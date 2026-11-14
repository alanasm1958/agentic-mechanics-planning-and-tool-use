// Tiny helper that drives a real headless Chromium through the DevTools protocol.
// Used because the shared Playwright MCP browser blocks file:// URLs and was being
// navigated by another session during testing. No packages needed (Node 24 has WebSocket).
import { spawn } from "node:child_process";
import { mkdtempSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";

const CHROME = process.env.CHROME_BIN ||
  `${process.env.HOME}/Library/Caches/ms-playwright/chromium_headless_shell-1248/chrome-headless-shell-mac-arm64/chrome-headless-shell`;

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

export async function launch(url, { width = 1280, height = 900, mobile = false } = {}) {
  const profile = mkdtempSync(join(process.env.TMPDIR || tmpdir(), "mp-profile-"));
  const port = 9300 + Math.floor(Math.random() * 500);
  const proc = spawn(CHROME, [
    `--remote-debugging-port=${port}`, `--user-data-dir=${profile}`,
    "--no-first-run", "--allow-file-access-from-files", "about:blank"
  ], { stdio: "ignore" });

  let pages = null;
  for (let i = 0; i < 50 && !pages; i++) {
    try { pages = await (await fetch(`http://127.0.0.1:${port}/json/list`)).json(); }
    catch { await sleep(100); }
  }
  if (!pages) throw new Error("Chromium did not start");
  const page = pages.find((p) => p.type === "page");
  const ws = new WebSocket(page.webSocketDebuggerUrl);
  await new Promise((res, rej) => { ws.onopen = res; ws.onerror = rej; });

  let nextId = 1;
  const pending = new Map();
  const errors = [];
  const dialogs = [];
  ws.onmessage = (ev) => {
    const msg = JSON.parse(ev.data);
    if (msg.id && pending.has(msg.id)) {
      const { res, rej } = pending.get(msg.id);
      pending.delete(msg.id);
      msg.error ? rej(new Error(msg.error.message)) : res(msg.result);
    } else if (msg.method === "Runtime.exceptionThrown") {
      errors.push(msg.params.exceptionDetails.exception?.description || msg.params.exceptionDetails.text);
    } else if (msg.method === "Runtime.consoleAPICalled" && ["error", "warning"].includes(msg.params.type)) {
      errors.push(`console.${msg.params.type}: ` + msg.params.args.map((a) => a.value ?? a.description).join(" "));
    } else if (msg.method === "Page.javascriptDialogOpening") {
      dialogs.push(msg.params.message);
      send("Page.handleJavaScriptDialog", { accept: true });
    }
  };
  function send(method, params = {}) {
    const id = nextId++;
    ws.send(JSON.stringify({ id, method, params }));
    return new Promise((res, rej) => pending.set(id, { res, rej }));
  }

  await send("Page.enable");
  await send("Runtime.enable");
  await setViewport(width, height, mobile);
  await goto(url);

  async function setViewport(w, h, isMobile = false) {
    await send("Emulation.setDeviceMetricsOverride", { width: w, height: h, deviceScaleFactor: 1, mobile: isMobile });
  }
  async function goto(u) {
    await send("Page.navigate", { url: u });
    for (let i = 0; i < 50; i++) {
      await sleep(100);
      if (await evaluate("document.readyState") === "complete") break;
    }
    await sleep(150);
  }
  async function evaluate(expression) {
    const r = await send("Runtime.evaluate", { expression, returnByValue: true, awaitPromise: true });
    if (r.exceptionDetails) throw new Error("Page error: " + (r.exceptionDetails.exception?.description || r.exceptionDetails.text));
    return r.result.value;
  }
  async function screenshot(path, fullPage = true) {
    const params = { format: "png" };
    if (fullPage) {
      const m = await send("Page.getLayoutMetrics");
      params.clip = { x: 0, y: 0, width: m.cssContentSize.width, height: m.cssContentSize.height, scale: 1 };
      params.captureBeyondViewport = true;
    }
    const { data } = await send("Page.captureScreenshot", params);
    writeFileSync(path, Buffer.from(data, "base64"));
  }
  async function pdf(path) {
    const { data } = await send("Page.printToPDF", { printBackground: false });
    writeFileSync(path, Buffer.from(data, "base64"));
  }
  async function reload() { await send("Page.reload"); await sleep(500); }
  async function close() {
    // Browser.close never answers (the socket just closes), so do not wait on it for long.
    await Promise.race([send("Browser.close").catch(() => {}), sleep(500)]);
    try { ws.close(); } catch { /* already closed */ }
    proc.kill();
  }

  return { send, evaluate, screenshot, pdf, goto, reload, setViewport, close, errors, dialogs, sleep };
}

// Simulates a person choosing an option in a dropdown: focus, change value, fire events.
export function pickJs(selector, optionText) {
  return `(() => {
    const s = document.querySelector(${JSON.stringify(selector)});
    if (!s) throw new Error("No element " + ${JSON.stringify(selector)});
    const opt = Array.from(s.options).find(o => o.textContent === ${JSON.stringify(optionText)});
    if (!opt) throw new Error("No option " + ${JSON.stringify(optionText)});
    s.focus(); s.value = opt.value;
    s.dispatchEvent(new Event("input", { bubbles: true }));
    s.dispatchEvent(new Event("change", { bubbles: true }));
    return s.value;
  })()`;
}

// Types into an input like a person would (sets value and fires input/change).
export function typeJs(selector, text) {
  return `(() => {
    const el = document.querySelector(${JSON.stringify(selector)});
    if (!el) throw new Error("No element " + ${JSON.stringify(selector)});
    el.focus(); el.value = ${JSON.stringify(text)};
    el.dispatchEvent(new Event("input", { bubbles: true }));
    el.dispatchEvent(new Event("change", { bubbles: true }));
    return el.value;
  })()`;
}

export const readListJs = `Array.from(document.querySelectorAll("#shopping li")).filter(li => li.querySelector(".name"))
  .map(li => li.querySelector(".name").textContent + " = " + li.querySelector(".amount").textContent)`;
