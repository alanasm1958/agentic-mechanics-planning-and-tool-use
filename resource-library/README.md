# Resource Library

This is a curated reading and watching list for the beginner training module "Agentic Mechanics: Planning and Tool Use." Every entry is tagged so you can pick what fits you: a level tag shows how demanding it is, and an access tag shows what it takes to open it. Level tags: `[intro]` is approachable for a non-coder, `[core]` is central reading worth your time, and `[deep]` is advanced or research-grade. Access tags: `[free]` opens with no barrier, `[paywalled]` needs a purchase, and `[account-required]` needs a free sign-up or login.

## Start here

A gentle on-ramp of resources that are both beginner-friendly and free. Start with any of these before going deeper.

- **What is an Agent? (Hugging Face Agents Course, Unit 1)** (Hugging Face, 2025) `[intro]` `[course]` `[free]`
  https://huggingface.co/learn/agents-course/en/unit1/what-are-agents
  A plain-language definition of an AI agent using a brain (the AI model that reasons and plans) and body (the tools it can act with) analogy. The cleanest starting point for a non-coder to grasp what an agent actually is.
- **Understanding AI Agents through the Thought-Action-Observation Cycle** (Hugging Face, 2025) `[intro]` `[course]` `[free]`
  https://huggingface.co/learn/agents-course/en/unit1/agent-steps-and-structure
  Walks through the core agent loop, thinking about the next step, acting by calling a tool, then observing the result, using a simple weather-agent example. It makes the plan, act, observe cycle concrete.
- **How tool use works** (Anthropic / Claude Platform Docs, 2026) `[intro]` `[docs]` `[free]`
  https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works
  A plain-language explanation of the tool-use loop as a contract where the model emits a request, your code runs it, and the result flows back into the conversation. The clearest single page on the agentic loop for beginners.
- **What is the Model Context Protocol (MCP)?** (modelcontextprotocol.io, 2025) `[intro]` `[docs]` `[free]`
  https://modelcontextprotocol.io/docs/getting-started/intro
  The official one-page introduction that defines MCP as a "USB-C port for AI applications" and explains what it enables. The clearest plain-language answer to "what is MCP" for a beginner.
- **AI Agents, Clearly Explained (Jeff Su)** (YouTube (Jeff Su), 2025) `[intro]` `[video]` `[free]`
  https://www.youtube.com/watch?v=FwOTs4UxQS4
  A short, jargon-free video that builds up from plain LLMs to AI workflows to true agents, then shows how tool use and the reason-and-act loop let an agent take real actions. An ideal first watch for non-coders.
- **AI Agents for Beginners (Microsoft)** (Microsoft (GitHub Pages), 2025) `[intro]` `[course]` `[free]`
  https://microsoft.github.io/ai-agents-for-beginners/
  A free, open-source course of short lessons, each with a written guide and a short video, including dedicated lessons on the Tool Use Design Pattern and the Planning Design Pattern. Fully open with no login.
- **Chain-of-Thought Prompting (Prompt Engineering Guide)** (Prompt Engineering Guide (promptingguide.ai), 2024) `[intro]` `[guide]` `[free]`
  https://www.promptingguide.ai/techniques/cot
  A short, example-driven explainer of chain-of-thought, including the simple zero-shot trick of adding "Let's think step by step." Ideal for non-coders who want to see the idea in plain terms.
- **What Are AI Agents?** (IBM Think, 2024) `[intro]` `[article]` `[free]`
  https://www.ibm.com/think/topics/ai-agents
  A beginner-friendly overview that explains how agents use an LLM plus external tools and the ReAct style Think-Act-Observe loop to solve tasks step by step. An accessible reinforcement of the agent loop.

## Foundations

- **What is an Agent? (Hugging Face Agents Course, Unit 1)** (Hugging Face, 2025) `[intro]` `[course]` `[free]`
  https://huggingface.co/learn/agents-course/en/unit1/what-are-agents
  A plain-language definition of an AI agent using a brain (the AI model that reasons and plans) and body (the tools it can act with) analogy. This is the cleanest starting point for a non-coder to grasp what an agent actually is before anything else.
- **Understanding AI Agents through the Thought-Action-Observation Cycle** (Hugging Face, 2025) `[intro]` `[course]` `[free]`
  https://huggingface.co/learn/agents-course/en/unit1/agent-steps-and-structure
  Walks through the core agent loop, thinking about the next step, acting by calling a tool, then observing the result, using a simple weather-agent example. It makes the plan, act, observe cycle concrete and is directly on-topic for this module.
- **What are AI Agents? Agents in Artificial Intelligence Explained** (Amazon Web Services (AWS), 2024) `[intro]` `[article]` `[free]`
  https://aws.amazon.com/what-is/ai-agents/
  An authoritative vendor-neutral overview defining an agent and its core parts: the foundation model as reasoning engine, memory, tools, and a planning module working in a perceive-reason-act feedback loop. A good second read that names the building blocks every agent shares.
- **What Are AI Agents?** (IBM Think, 2024) `[intro]` `[article]` `[free]`
  https://www.ibm.com/think/topics/ai-agents
  A beginner-friendly overview that explains how agents use an LLM plus external tools and the ReAct style Think-Act-Observe loop to solve tasks step by step. A useful, accessible reinforcement of the agent loop.
- **Building Effective Agents** (Anthropic, 2024) `[core]` `[guide]` `[free]`
  https://www.anthropic.com/engineering/building-effective-agents
  The reference explanation of the difference between a workflow (LLMs and tools run through predefined code paths) and an agent (the model dynamically directs its own steps and tool use). Central reading for this module because it draws the workflow versus agent line precisely and advises starting simple.
- **A Practical Guide to Building Agents** (OpenAI, 2025) `[core]` `[guide]` `[free]`
  https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
  A freely downloadable guide that defines what an agent is, when a task warrants one rather than a simple workflow, and the core components (model, tools, instructions). Pairs well with the Anthropic piece to give learners two authoritative views on the same distinction.
- **AI Agents Course: Introduction and Onboarding (Unit 0)** (Hugging Face, 2025) `[core]` `[course]` `[free]`
  https://huggingface.co/learn/agents-course/en/unit0/introduction
  The free, structured onboarding for Hugging Face's full agents course, taking learners from beginner to building working agents with hands-on units. Worth flagging as a guided path for anyone who wants to go beyond a single explainer.
- **A Survey on Large Language Model based Autonomous Agents** (arXiv (Wang et al.), 2023) `[deep]` `[paper]` `[free]`
  https://arxiv.org/abs/2308.11432
  The landmark academic survey that organizes LLM agents into a unified framework of profile, memory, planning, and action. Included as the authoritative deep reference for learners who want the rigorous map behind the beginner explainers; the abstract and PDF are open access.

## Planning

- **Chain-of-Thought Prompting (Prompt Engineering Guide)** (Prompt Engineering Guide (promptingguide.ai), 2024) `[intro]` `[guide]` `[free]`
  https://www.promptingguide.ai/techniques/cot
  A short, example-driven explainer of chain-of-thought, including the simple zero-shot trick of adding "Let's think step by step." Ideal for non-coders who want to see the idea in plain terms before reading the original paper.
- **ReAct Prompting (Prompt Engineering Guide)** (Prompt Engineering Guide (promptingguide.ai), 2024) `[intro]` `[guide]` `[free]`
  https://www.promptingguide.ai/techniques/react
  A plain-language walkthrough of the ReAct loop of thought, action, and observation, with a worked example. Good for beginners to grasp how reasoning and tool use interleave before diving into the research paper.
- **Agentic Design Patterns Part 2: Reflection** (DeepLearning.AI, The Batch (Andrew Ng), 2024) `[intro]` `[article]` `[free]`
  https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-2-reflection/
  Andrew Ng's approachable letter explaining the reflection pattern as a generate, critique, and revise loop. A great non-technical entry point to self-reflection that frames why it works and when to use it.
- **Beginner's Guide To Tree Of Thoughts Prompting (With Examples)** (Zero To Mastery, 2024) `[intro]` `[tutorial]` `[free]`
  https://zerotomastery.io/blog/tree-of-thought-prompting/
  A beginner-friendly explainer of Tree of Thoughts using the Game of 24 example, contrasting its 74 percent success against chain-of-thought's 4 percent. It makes the abstract idea of branching and backtracking concrete for non-coders. Note: the page promotes a paid course, but the article itself is free.
- **Chain-of-Thought Prompting Elicits Reasoning in Large Language Models** (arXiv (Wei et al., Google Research), 2022) `[core]` `[paper]` `[free]`
  https://arxiv.org/abs/2201.11903
  The landmark paper showing that asking a model to write out intermediate reasoning steps sharply improves its problem solving. This is the foundation every other planning pattern builds on, so it is the natural starting point for the module.
- **ReAct: Synergizing Reasoning and Acting in Language Models** (arXiv (Yao et al., Princeton & Google), 2022) `[core]` `[paper]` `[free]`
  https://arxiv.org/abs/2210.03629
  The original paper for ReAct, the pattern where an agent alternates between reasoning and taking actions such as calling a tool or searching the web. This is arguably the single most important planning pattern for tool-using agents, which makes it central to this module.
- **Plan-and-Execute Agents** (LangChain Blog, 2024) `[core]` `[article]` `[free]`
  https://www.langchain.com/blog/planning-agents
  A clear practitioner explainer of how a planner LLM drafts a multi-step plan and an executor carries it out, with re-planning along the way. It connects the research idea to how real agent frameworks actually implement plan-and-execute, which is exactly what this module teaches.
- **Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models** (ACL Anthology (Wang et al., ACL 2023), 2023) `[deep]` `[paper]` `[free]`
  https://aclanthology.org/2023.acl-long.147/
  The peer-reviewed paper that introduced first making an explicit plan and then executing it, the academic basis for plan-and-execute agents. It matters here because it separates planning from doing, the core idea of the plan-and-execute pattern.
- **Reflexion: Language Agents with Verbal Reinforcement Learning** (arXiv (Shinn et al., NeurIPS 2023), 2023) `[deep]` `[paper]` `[free]`
  https://arxiv.org/abs/2303.11366
  The original Reflexion paper, where an agent reflects on its own failures in words and keeps those reflections in memory to do better next time. This is the canonical reference for the self-reflection pattern that lets agents learn from mistakes without retraining.
- **Tree of Thoughts: Deliberate Problem Solving with Large Language Models** (arXiv (Yao et al., Princeton & DeepMind, NeurIPS 2023), 2023) `[deep]` `[paper]` `[free]`
  https://arxiv.org/abs/2305.10601
  The original Tree of Thoughts paper, which lets a model explore several reasoning branches, evaluate them, and backtrack rather than committing to one chain. It shows the advanced end of planning, where an agent searches over possibilities instead of marching straight ahead.

## Tool use

- **How tool use works** (Anthropic / Claude Platform Docs, 2026) `[intro]` `[docs]` `[free]`
  https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works
  A plain-language explanation of the tool-use loop as a contract where the model emits a request, your code runs it, and the result flows back into the conversation. The clearest single page on the agentic loop and when tools are or are not the right approach, ideal for beginners.
- **What is Function Calling?** (Hugging Face AI Agents Course (Bonus Unit 1), 2025) `[intro]` `[course]` `[free]`
  https://huggingface.co/learn/agents-course/bonus-unit1/what-is-function-calling
  A beginner-friendly lesson framing function calling as a way for an LLM to take actions, walking through the think-act-observe cycle with concrete examples. A gentle on-ramp for non-coders before they meet provider-specific APIs.
- **Function Calling in AI Agents** (Prompt Engineering Guide (DAIR.AI), 2025) `[intro]` `[guide]` `[free]`
  https://www.promptingguide.ai/agents/function-calling
  A vendor-neutral explainer with diagrams covering what function calling is, how tool definitions work, and the action-observation loop. Approachable for beginners and good for understanding the concept independent of any one provider.
- **Tool use with Claude (Overview)** (Anthropic / Claude Platform Docs, 2026) `[core]` `[docs]` `[free]`
  https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview
  The official Anthropic starting point for tool use, showing how Claude decides to call a tool and returns a structured tool_use request your app executes. This is the canonical reference for the module and distinguishes client tools you run from server tools Anthropic runs.
- **Handle tool calls (tool_result and error handling)** (Anthropic / Claude Platform Docs, 2026) `[core]` `[docs]` `[free]`
  https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls
  Shows the full round trip: parsing tool_use blocks, formatting tool_result replies, and returning errors with is_error so the model can recover. The go-to reference for the structured handshake and error handling parts of this module.
- **Function calling (OpenAI API guide)** (OpenAI Developer Docs, 2026) `[core]` `[docs]` `[free]`
  https://developers.openai.com/api/docs/guides/function-calling
  OpenAI's official guide laying out the five-step function calling workflow and JSON schema tool definitions. Pairing it with the Anthropic docs shows learners that the tool-use pattern is consistent across providers.
- **Structured model outputs (OpenAI API guide)** (OpenAI Developer Docs, 2026) `[core]` `[docs]` `[free]`
  https://developers.openai.com/api/docs/guides/structured-outputs
  Explains how to force a model's response to conform exactly to a JSON Schema so you get reliable, typed data instead of free-form text. Directly covers the structured outputs portion of this module and why schema conformance matters.
- **The Guide to Structured Outputs and Function Calling with LLMs** (Agenta, 2026) `[core]` `[article]` `[free]`
  https://agenta.ai/blog/the-guide-to-structured-outputs-and-function-calling-with-llms
  Clarifies the often-confused distinction between structured outputs (forcing a data shape) and function calling (deciding which tool to invoke), with examples across Claude, GPT, and Gemini. Helpful for learners who need both concepts disentangled in one place.
- **Introducing advanced tool use on the Claude Developer Platform** (Anthropic Engineering, 2025) `[deep]` `[article]` `[free]`
  https://www.anthropic.com/engineering/advanced-tool-use
  Anthropic's engineering post on tool search, programmatic tool calling, and tool use examples for agents working across many tools. Useful for learners who want to see where tool use is heading once a basic loop is understood.
- **Toolformer: Language Models Can Teach Themselves to Use Tools** (arXiv (Schick et al., Meta AI), 2023) `[deep]` `[paper]` `[free]`
  https://arxiv.org/abs/2302.04761
  The landmark paper showing that a language model can learn which APIs to call, when, and with what arguments in a self-supervised way. Included as the foundational reference behind today's tool-use capabilities; skimmable abstract is enough for beginners.

## Model Context Protocol (MCP)

- **What is the Model Context Protocol (MCP)?** (modelcontextprotocol.io (official docs), 2025) `[intro]` `[docs]` `[free]`
  https://modelcontextprotocol.io/docs/getting-started/intro
  The official one-page introduction that defines MCP as a "USB-C port for AI applications" and explains what it enables for developers, AI apps, and end users. This is the canonical starting point and the clearest plain-language answer to "what is MCP" for a beginner.
- **Introducing the Model Context Protocol** (Anthropic, 2024) `[intro]` `[article]` `[free]`
  https://www.anthropic.com/news/model-context-protocol
  Anthropic's original November 2024 announcement that launched MCP, explaining why it exists: AI models are trapped behind information silos and every new data source used to need its own custom integration. This is the foundational primary source for the "why" behind the protocol.
- **Model Context Protocol** (Wikipedia, 2026) `[intro]` `[article]` `[free]`
  https://en.wikipedia.org/wiki/Model_Context_Protocol
  A neutral, continuously updated overview covering MCP's origin, architecture, adoption by OpenAI and Google, and its 2025 donation to the Linux Foundation's Agentic AI Foundation. Useful for beginners who want the history and current state of the ecosystem in one vendor-neutral place.
- **What is Model Context Protocol (MCP)? A guide** (Google Cloud, 2025) `[intro]` `[article]` `[free]`
  https://cloud.google.com/discover/what-is-model-context-protocol
  A short, accessible vendor explainer from a major cloud provider that frames MCP as a model-agnostic universal connector for AI systems. A good second perspective that reassures beginners MCP is an industry-wide standard, not a single-company feature.
- **MCP 101: An Introduction to Model Context Protocol** (DigitalOcean, 2025) `[intro]` `[tutorial]` `[free]`
  https://www.digitalocean.com/community/tutorials/model-context-protocol
  A free, deliberately beginner-oriented tutorial that explains MCP's roots in the Language Server Protocol, its host/client/server architecture, and why it improves reliability and safety. Strikes a nice balance between approachable framing and enough technical depth to feel concrete.
- **Architecture overview (core concepts)** (modelcontextprotocol.io (official docs), 2025) `[core]` `[docs]` `[free]`
  https://modelcontextprotocol.io/docs/learn/architecture
  The official concepts page that walks through the host, client, and server roles plus the three server primitives of tools, resources, and prompts, with a worked example. Central reading for understanding how the pieces actually fit together once the basic idea clicks.
- **Introduction to Model Context Protocol** (Anthropic Academy (Skilljar), 2025) `[core]` `[course]` `[account-required]`
  https://anthropic.skilljar.com/introduction-to-model-context-protocol
  Anthropic's free official course teaching the three core primitives (tools, resources, prompts) and how to build MCP servers and clients. Requires a free registration and some Python familiarity, making it the natural next step for learners ready to go hands-on.
- **MCP: Build Rich-Context AI Apps with Anthropic** (DeepLearning.AI, 2025) `[core]` `[course]` `[account-required]`
  https://learn.deeplearning.ai/courses/mcp-build-rich-context-ai-apps-with-anthropic/lesson/fkbhh/introduction
  A free-to-audit short course built with Anthropic and taught by its Head of Technical Education, covering MCP's client-server model and how to build and connect MCP servers. Excellent structured video learning for beginners who prefer a guided walkthrough over reading docs.

## Building and evaluating agents

- **A Practical Guide to Building Agents** (OpenAI, 2025) `[intro]` `[guide]` `[free]`
  https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
  A concise, approachable PDF that breaks an agent into three parts (model, tools, instructions) and walks through when to build one, single versus multi-agent orchestration, and guardrails. Written for product and engineering teams new to agents, it is a friendly counterpart to Anthropic's guide for non-coders.
- **Agentic Workflows: Emerging Architectures and Design Patterns** (Vellum, 2025) `[intro]` `[article]` `[free]`
  https://www.vellum.ai/blog/agentic-workflows-emerging-architectures-and-design-patterns
  A clear survey of single-agent and multi-agent design patterns that frames agency as levels of decision-making and is honest about current production limitations. A good plain-language overview of orchestration shapes for readers who want the landscape before diving into specifics.
- **AI Agents Course** (Hugging Face, 2025) `[intro]` `[course]` `[account-required]`
  https://huggingface.co/learn/agents-course/unit0/introduction
  A free, beginner-to-expert hands-on course that teaches the agent loop (thought, action, observation), tool use, and how to build and evaluate agents with frameworks like smolagents and LangGraph. It is the most practical starting point for non-coders who want to actually build something, though it asks for a free Hugging Face account.
- **Building Effective Agents** (Anthropic, 2024) `[core]` `[guide]` `[free]`
  https://www.anthropic.com/engineering/building-effective-agents
  Anthropic's landmark practitioner guide that defines the core agent building blocks and five workflow patterns: prompt chaining, routing, parallelization, orchestrator-workers, and evaluator-optimizer. It is the standard reference for this module and its central message of starting simple and only adding complexity when it pays off is exactly the mindset beginners need.
- **How We Built Our Multi-Agent Research System** (Anthropic Engineering, 2025) `[core]` `[article]` `[free]`
  https://www.anthropic.com/engineering/multi-agent-research-system
  A candid engineering writeup of a real production multi-agent system built on the orchestrator-worker pattern, including how it was evaluated and why multi-agent setups can use roughly 15 times more tokens than a single chat. It makes the cost, latency, and reliability tradeoffs of orchestration shapes concrete instead of abstract.
- **Agents** (Chip Huyen (huyenchip.com), 2025) `[core]` `[article]` `[free]`
  https://huyenchip.com/2025/01/07/agents.html
  An 8,000-word deep dive, adapted from the AI Engineering book, on what makes an agent work: tool selection, planning, control flow, and the common failure modes. It is the best single piece for understanding why planning and tool use are the two levers that determine agent capability.
- **Building Effective Agents Cookbook (reference implementations)** (Anthropic (GitHub claude-cookbooks), 2024) `[core]` `[tutorial]` `[free]`
  https://github.com/anthropics/anthropic-cookbook/tree/main/patterns/agents
  The companion code to Anthropic's guide, with runnable Jupyter notebooks for each pattern: prompt chaining, routing, parallelization, orchestrator-workers, and evaluator-optimizer. It lets learners see each orchestration shape as minimal working code rather than only as a diagram.
- **LLM Evaluation Framework: Trajectories vs. Outputs** (LangChain, 2025) `[core]` `[article]` `[free]`
  https://www.langchain.com/resources/llm-evaluation-framework
  A focused explainer on why evaluating only an agent's final answer misses the tool calls and reasoning steps where agents actually fail, and how trajectory evaluation fixes that. It gives beginners a clear mental model for the single most important idea in agent evaluation.
- **Agent Evaluation: A Detailed Guide** (Cameron R. Wolfe, Deep (Learning) Focus, 2026) `[deep]` `[article]` `[free]`
  https://cameronrwolfe.substack.com/p/agent-evals
  A thorough, well-structured walkthrough of how to actually evaluate agents, covering tasks, transcripts, graders, code versus model-based versus human grading, Pass@K and Pass^K reliability metrics, and real benchmarks. It is the go-to reference for the evaluation half of this subtopic and shows why measuring agents is harder than measuring a single prompt.

## Beginner videos and courses

- **AI Agents, Clearly Explained (Jeff Su)** (YouTube (Jeff Su), 2025) `[intro]` `[video]` `[free]`
  https://www.youtube.com/watch?v=FwOTs4UxQS4
  A short, jargon-free video that builds up from plain LLMs to AI workflows to true agents, then shows how tool use and the reason-and-act loop let an agent take real actions. An ideal first watch for non-coders to grasp what "agentic" means before any hands-on work.
- **What are AI Agents? (IBM Technology)** (YouTube (IBM Technology), 2024) `[intro]` `[video]` `[free]`
  https://www.youtube.com/watch?v=F8NKVhkZZWI
  An IBM expert explains, with simple diagrams, how an agent designs its own workflow and uses external tools and databases to complete tasks. A reputable, vendor-neutral overview that reinforces the planning and tool-use ideas at the heart of this module.
- **AI Agents for Beginners (Microsoft)** (Microsoft (GitHub Pages), 2025) `[intro]` `[course]` `[free]`
  https://microsoft.github.io/ai-agents-for-beginners/
  A free, open-source course of short lessons, each with a written guide and a short video, including dedicated lessons on the Tool Use Design Pattern and the Planning Design Pattern. Fully open with no login, making it one of the most accessible structured options for this subtopic.
- **What is the Model Context Protocol (MCP)?** (Model Context Protocol (official docs), 2025) `[intro]` `[docs]` `[free]`
  https://modelcontextprotocol.io/docs/getting-started/intro
  The official, plain-language introduction to MCP that uses a USB-C analogy to explain how agents connect to tools, data, and services in a standard way. A short, free read that demystifies the plumbing behind modern tool use for complete beginners.
- **Hugging Face AI Agents Course** (Hugging Face, 2025) `[intro]` `[course]` `[account-required]`
  https://huggingface.co/learn/agents-course/en/unit0/introduction
  A free, certified course that takes you from beginner to building real agents, with Unit 1 teaching the core loop of Tools, Thoughts, Actions, and Observations. It needs a free account but is the most complete structured path here for learners ready to go hands-on.
- **AI Agentic Design Patterns with AutoGen (DeepLearning.AI short course)** (DeepLearning.AI, 2024) `[intro]` `[course]` `[account-required]`
  https://www.deeplearning.ai/courses/ai-agentic-design-patterns-with-autogen
  A roughly 90-minute beginner course, taught by AutoGen's creators, that walks through the four agentic patterns: reflection, tool use, planning, and multi-agent collaboration. Free to audit and the patterns it names map almost exactly onto this module's focus on planning and tool use.
- **Building Effective Agents (Anthropic)** (Anthropic, 2024) `[core]` `[guide]` `[free]`
  https://www.anthropic.com/engineering/building-effective-agents
  Anthropic's widely cited guide that clearly separates predefined workflows from autonomous agents and lays out simple building blocks for tool use and planning. Beginners can read it for the vocabulary and mental models even if they skip the code, and it is the standard reference practitioners point to.
- **Introduction to Agents (Kaggle and Google whitepaper)** (Kaggle and Google, 2025) `[core]` `[guide]` `[free]`
  https://www.kaggle.com/whitepaper-introduction-to-agents
  A free companion whitepaper from Google and Kaggle's 5-Day AI Agents Intensive that explains agent architecture, tools, and planning in an approachable way. A solid primary reading to pair with the videos, with no registration or payment required.
- **Agentic AI (DeepLearning.AI, taught by Andrew Ng)** (DeepLearning.AI, 2025) `[core]` `[course]` `[account-required]`
  https://www.deeplearning.ai/courses/agentic-ai
  Andrew Ng's course on building agentic systems, structured around modules for reflection, tool use, and planning for highly autonomous agents. Free to audit (videos and community) and a strong next step once learners are comfortable with the basics, though it leans intermediate.

## Responsible AI and the development context

- **AI for Good Global Platform (About)** (International Telecommunication Union (ITU), 2026) `[intro]` `[article]` `[free]`
  https://aiforgood.itu.int/about-us/
  The UN's main action platform for applying AI to the Sustainable Development Goals, run by ITU with 40-plus UN agencies. A friendly entry point showing concrete, real-world AI-for-good projects for a non-technical audience.
- **UNDP and AI for Sustainable Development** (UNDP via ITU AI for Good, 2024) `[intro]` `[article]` `[free]`
  https://aiforgood.itu.int/about-us/un-ai-actions/undp/
  An overview of how UNDP, the UN's lead development agency, uses AI for poverty mapping, crisis response, and detecting election misinformation across 170 countries. It grounds responsible AI in tangible development use cases relevant to this audience.
- **AI, Justice and the Rule of Law (Free MOOC)** (UNESCO and University of Oxford, 2026) `[intro]` `[course]` `[free]`
  https://www.unesco.org/en/articles/unesco-and-university-oxford-launch-free-global-course-ai-and-rule-law
  A free, self-paced course requiring no technical background that gives a human-rights-based framework for evaluating AI systems, with a practical checklist. Ideal hands-on learning for public-sector beginners who want to scrutinize AI responsibly.
- **Recommendation on the Ethics of Artificial Intelligence** (UNESCO, 2021) `[core]` `[guide]` `[free]`
  https://www.unesco.org/en/artificial-intelligence/recommendation-ethics
  The first global standard on AI ethics, adopted by all 193 UNESCO member states, built on human rights, transparency, fairness, and human oversight. It is the foundational reference any public-sector learner should know when thinking about responsible AI.
- **Governing AI for Humanity: Final Report of the UN High-Level Advisory Body on AI** (United Nations, 2024) `[core]` `[paper]` `[free]`
  https://www.un.org/en/ai-advisory-body
  The UN's flagship report on global AI governance, warning that most countries are excluded from current AI rule-making and proposing inclusive mechanisms. It frames why governing AI fairly matters for development and the Global South.
- **OECD AI Principles** (OECD, 2024) `[core]` `[guide]` `[free]`
  https://oecd.ai/en/ai-principles
  The first intergovernmental AI standard, with five plain-language values for trustworthy AI such as transparency, accountability, and respect for human rights. Widely adopted and a clear, beginner-readable complement to the UNESCO Recommendation.
- **Readiness Assessment Methodology (RAM): A Tool of the Recommendation on the Ethics of AI** (UNESCO, 2023) `[core]` `[guide]` `[free]`
  https://www.unesco.org/ethics-ai/en/ram
  UNESCO's practical tool that helps governments assess how prepared they are to govern AI responsibly across legal, social, and technical dimensions. It shows learners how high-level ethics principles get turned into concrete national action.
- **B-Tech Project: Applying Human Rights to AI and Digital Technologies** (UN Human Rights (OHCHR), 2024) `[core]` `[guide]` `[free]`
  https://www.ohchr.org/en/b-tech
  UN Human Rights guidance, including a dedicated generative-AI workstream, on how the Guiding Principles on Business and Human Rights apply to AI development and use. Essential for understanding the human-rights dimension of responsible AI in practice.
- **The role of artificial intelligence in achieving the Sustainable Development Goals** (Vinuesa et al., Nature Communications (open access via PMC), 2020) `[deep]` `[paper]` `[free]`
  https://pmc.ncbi.nlm.nih.gov/articles/PMC6957485/
  The landmark peer-reviewed study finding that AI can help advance 134 of the SDG targets but may also inhibit 59, depending on governance. The standard academic reference for the dual-use, opportunity-and-risk framing at the heart of AI for development.

## Keeping this current

Links and tools in this fast-moving field go stale quickly, so revisit this library every few months to confirm each link still works and still reflects current guidance. Replace anything that has moved, been deprecated, or been superseded by a clearer or more current resource, and prune entries that no longer earn their place.
