"""Render cafe_promo.mp4: 1080x1920, 30 s, 30 fps, five animated text scenes. Pillow frames piped to ffmpeg."""
import math
import subprocess
import sys
from functools import lru_cache
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent.parent
OUT = HERE / "cafe_promo.mp4"
W, H, FPS, SCENE, FADE = 1080, 1920, 30, 6.0, 0.5
TOTAL_FRAMES = int(5 * SCENE * FPS)
FONT_PATH = "/System/Library/Fonts/Supplemental/Arial Rounded Bold.ttf"
MAX_TEXT_W = 900  # keeps 90 px clear on each side

CREAM = (255, 244, 230)
TERRACOTTA = (196, 82, 58)
COFFEE = (74, 46, 33)
MUSTARD = (242, 165, 65)
PEACH = (246, 189, 154)
WHITE = (255, 255, 255)
SHADOW = (236, 219, 198)

# Facts taken from summary.md and the brief
TOP_PRODUCT, TOP_CUPS = "Cappuccino", 3259
FAVOURITES = ["Latte", "Chicken Sandwich", "Croissant"]
BUSIEST, QUIETEST = "Saturday", "Monday"
HOURS = "07:00 to 19:00"


def clamp(x, lo=0.0, hi=1.0):
    return max(lo, min(hi, x))


def ease(x):
    x = clamp(x)
    return 1 - (1 - x) ** 3


def prog(t, start, dur=0.7):
    return ease((t - start) / dur)


@lru_cache(maxsize=None)
def font(size):
    return ImageFont.truetype(FONT_PATH, size)


def fit(text, size, max_w=MAX_TEXT_W):
    while font(size).getlength(text) > max_w and size > 20:
        size -= 2
    return size


@lru_cache(maxsize=None)
def text_sprite(text, size, color):
    f = font(size)
    l, t, r, b = f.getbbox(text)
    pad = 6
    img = Image.new("RGBA", (r - l + 2 * pad, b - t + 2 * pad), color + (0,))
    ImageDraw.Draw(img).text((pad - l, pad - t), text, font=f, fill=color + (255,))
    return img


@lru_cache(maxsize=None)
def circle_sprite(d, color):
    s = 4
    big = Image.new("RGBA", (d * s, d * s), color + (0,))
    ImageDraw.Draw(big).ellipse((0, 0, d * s - 1, d * s - 1), fill=color + (255,))
    return big.resize((d, d), Image.LANCZOS)


@lru_cache(maxsize=None)
def pill_sprite(w, h, color):
    s = 4
    big = Image.new("RGBA", (w * s, h * s), color + (0,))
    ImageDraw.Draw(big).rounded_rectangle((0, 0, w * s - 1, h * s - 1), radius=h * s // 2, fill=color + (255,))
    return big.resize((w, h), Image.LANCZOS)


@lru_cache(maxsize=None)
def cup_sprite():
    s, w, h = 4, 640, 420
    img = Image.new("RGBA", (w * s, h * s), WHITE + (0,))
    d = ImageDraw.Draw(img)
    S = lambda *v: tuple(int(x * s) for x in v)
    d.ellipse(S(20, 330, 620, 410), fill=SHADOW + (255,))            # saucer
    d.ellipse(S(470, 120, 600, 260), outline=WHITE + (255,), width=34 * s)  # handle
    d.rounded_rectangle(S(110, 40, 530, 360), radius=110 * s, fill=WHITE + (255,))  # body
    d.rectangle(S(110, 40, 530, 150), fill=WHITE + (255,))
    d.ellipse(S(110, 10, 530, 80), fill=WHITE + (255,))              # rim
    d.ellipse(S(130, 22, 510, 70), fill=(214, 170, 120, 255))        # coffee foam
    return img.resize((w, h), Image.LANCZOS)


def put(frame, sprite, cx, cy, opacity=1.0):
    if opacity <= 0.003:
        return
    if opacity < 0.997:
        alpha = sprite.getchannel("A").point(lambda a: int(a * opacity))
    else:
        alpha = sprite.getchannel("A")
    frame.paste(sprite, (int(round(cx - sprite.width / 2)), int(round(cy - sprite.height / 2))), alpha)


def put_text(frame, text, size, color, cx, cy, t, start, rise=60):
    p = prog(t, start)
    put(frame, text_sprite(text, fit(text, size), color), cx, cy + (1 - p) * rise, p)


def steam(frame, t, cx, top):
    layer = Image.new("RGBA", (600, 440), WHITE + (0,))
    d = ImageDraw.Draw(layer)
    for i, x0 in enumerate((180, 300, 420)):
        pts = [(x0 + 22 * math.sin(y / 55 + t * 3 + i * 1.7), 40 + y) for y in range(0, 300, 6)]
        d.line(pts, fill=WHITE + (150,), width=22, joint="curve")
    small = layer.resize((300, 220), Image.LANCZOS)
    put(frame, small, cx, top + 110, prog(t, 1.0, 1.0))


def scene_hello(t):
    f = Image.new("RGB", (W, H), CREAM)
    for i, (x, y, d) in enumerate(((160, 300, 70), (930, 420, 50), (880, 1280, 40), (190, 1180, 56))):
        put(f, circle_sprite(d, PEACH), x, y + 12 * math.sin(t * 1.5 + i), prog(t, 0.2 + 0.15 * i))
    put(f, circle_sprite(980, MUSTARD), W / 2, 2500 - 820 * prog(t, 0.0, 1.6))
    put_text(f, "Hello,", 160, COFFEE, W / 2, 560, t, 0.4)
    put_text(f, "neighbour!", 160, TERRACOTTA, W / 2, 740, t, 0.8)
    put_text(f, "Welcome to", 76, COFFEE, W / 2, 960, t, 1.6)
    put_text(f, "Corner Café", 104, COFFEE, W / 2, 1075, t, 1.9)
    return f


def scene_number_one(t):
    f = Image.new("RGB", (W, H), TERRACOTTA)
    put_text(f, "Our number one", 76, CREAM, W / 2, 330, t, 0.3)
    put_text(f, TOP_PRODUCT, 150, WHITE, W / 2, 480, t, 0.6)
    steam(f, t, W / 2, 610)
    p = prog(t, 0.4, 0.8)
    put(f, cup_sprite(), W / 2, 1040 + (1 - p) * 80, p)
    n = int(round(TOP_CUPS * ease((t - 1.4) / 1.8))) if t > 1.4 else 0
    put_text(f, f"{n:,} cups", 130, WHITE, W / 2, 1400, t, 1.2)
    put_text(f, "in three months", 72, CREAM, W / 2, 1540, t, 1.6)
    return f


def scene_favourites(t):
    f = Image.new("RGB", (W, H), CREAM)
    put_text(f, "Neighbourhood", 112, COFFEE, W / 2, 540, t, 0.3)
    put_text(f, "favourites", 112, TERRACOTTA, W / 2, 680, t, 0.5)
    size = min(fit(name, 84, 620) for name in FAVOURITES)
    dots = (TERRACOTTA, MUSTARD, PEACH)
    for i, name in enumerate(FAVOURITES):
        p = prog(t, 1.0 + 0.45 * i, 0.8)
        cx, cy = W / 2 + (1 - p) * 1100, 950 + i * 250
        put(f, pill_sprite(900, 200, SHADOW), cx + 10, cy + 14, p)
        put(f, pill_sprite(900, 200, WHITE), cx, cy, p)
        put(f, circle_sprite(110, dots[i]), cx - 450 + 115, cy, p)
        sprite = text_sprite(name, size, COFFEE)
        put(f, sprite, cx - 450 + 200 + sprite.width / 2, cy, p)
    return f


def scene_busy(t):
    f = Image.new("RGB", (W, H), COFFEE)
    put_text(f, BUSIEST, 170, MUSTARD, W / 2, 500, t, 0.3)
    put_text(f, "is our busiest day", 84, CREAM, W / 2, 670, t, 0.6)
    letters = "MTWTFSS"
    grow = prog(t, 1.6, 0.6)
    calm = prog(t, 2.8, 0.6)
    for i, ch in enumerate(letters):
        p = prog(t, 0.9 + 0.08 * i, 0.5)
        cx, cy = W / 2 + (i - 3) * 138, 1010
        d, col, txt = 112, CREAM, COFFEE
        if i == 5:
            d, col = int(112 + 40 * grow), (MUSTARD if grow > 0.5 else CREAM)
        if i == 0 and calm > 0.5:
            col = PEACH
        put(f, circle_sprite(d, col), cx, cy + (1 - p) * 40, p)
        put(f, text_sprite(ch, 56 if i != 5 else int(56 + 16 * grow), txt), cx, cy + (1 - p) * 40, p)
    put_text(f, "Prefer it quiet?", 80, CREAM, W / 2, 1300, t, 2.6)
    put_text(f, f"Try a {QUIETEST}.", 80, PEACH, W / 2, 1410, t, 2.9)
    return f


def scene_visit(t):
    f = Image.new("RGB", (W, H), MUSTARD)
    for i, (x, y, d) in enumerate(((140, 230, 240), (990, 250, 170), (120, 1690, 220), (960, 1660, 300))):
        put(f, circle_sprite(d, PEACH), x + 20 * math.sin(t * 0.8 + i), y + 25 * math.cos(t * 0.7 + i), 0.75)
    for line, y, start in (("Corner", 520, 0.3), ("Café", 720, 0.55)):
        p = prog(t, start, 0.6)
        size = max(10, int(200 * (0.85 + 0.15 * p)))
        put(f, text_sprite(line, size, COFFEE), W / 2, y, p)
    put_text(f, "Open every day", 80, COFFEE, W / 2, 960, t, 1.2)
    p = prog(t, 1.6, 0.7)
    put(f, pill_sprite(840, 180, WHITE), W / 2, 1160 + (1 - p) * 60, p)
    put(f, text_sprite(HOURS, fit(HOURS, 100, 720), TERRACOTTA), W / 2, 1160 + (1 - p) * 60, p)
    put_text(f, "See you soon!", 84, COFFEE, W / 2, 1400, t, 2.3)
    return f


SCENES = [scene_hello, scene_number_one, scene_favourites, scene_busy, scene_visit]


def frame_at(g):
    i = min(int(g // SCENE), len(SCENES) - 1)
    t = g - i * SCENE
    cur = SCENES[i](t)
    if i > 0 and t < FADE:
        prev = SCENES[i - 1](SCENE + t)
        return Image.blend(prev, cur, ease(t / FADE))
    return cur


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--preview":
        out = Path(__file__).resolve().parent / "preview"
        out.mkdir(exist_ok=True)
        for g in (4.5, 10.5, 16.5, 22.5, 29.9):
            frame_at(g).save(out / f"preview_{g:04.1f}.png")
        return 0
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
           "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium",
           "-crf", "18", "-pix_fmt", "yuv420p", "-profile:v", "high", "-movflags", "+faststart",
           "-r", str(FPS), str(OUT)]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for n in range(TOTAL_FRAMES):
        proc.stdin.write(frame_at(n / FPS).tobytes())
    proc.stdin.close()
    code = proc.wait()
    print("ffmpeg exit code", code, "frames", TOTAL_FRAMES)
    return code


if __name__ == "__main__":
    sys.exit(main())
