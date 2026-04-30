# 🚀 MiMo Agent Hub

A multi-agent AI automation platform powered by **MiMo**, designed to solve complex real-world tasks through autonomous agent collaboration.

## ✨ Overview

MiMo Agent Hub is a developer-focused AI system that orchestrates multiple intelligent agents to plan, execute, and validate tasks automatically.

It is designed for:

- AI developers building autonomous workflows
- Code generation & automated software development
- Data analysis automation
- AI content pipelines

## 🧠 Architecture

The system consists of three core agents:

| Agent | Role |
|---|---|
| **Planner Agent** | Breaks down complex tasks into structured steps |
| **Executor Agent** | Executes tasks: code generation, data analysis, content creation |
| **Reviewer Agent** | Validates outputs and improves quality through iterative feedback |

### 🔁 Workflow

```
User Input → Planner → Executor → Reviewer → Final Output
                 ↑                           |
                 └───── Replan (if needed) ──┘
```

## ⚙️ Tech Stack

- **Python** (FastAPI) — REST API server
- **LangChain** — Agent orchestration (planned)
- **MiMo API** — LLM backbone
- **Docker** — Deployment-ready

## 📦 Use Cases

- Full-stack application generation
- Automated coding assistant
- AI content production pipelines
- Data analysis & reporting automation

## 🔌 MiMo Integration

This project is deeply integrated with **MiMo** for:

- Long-context reasoning across multi-step tasks
- Multi-agent communication with high-frequency API calls
- Autonomous task execution requiring sustained token consumption

**Currently testing high-frequency MiMo API calls for agent orchestration.**

Estimated token usage breakdown:

| Category | Allocation |
|---|---|
| Multi-agent interaction | ~60% |
| Code generation tasks | ~20% |
| Data processing & analysis | ~10% |
| Content generation | ~10% |

Expected total usage: **500M – 700M tokens/month**

## 📂 Project Structure

```
mimo-agent-hub/
├── agents/
│   ├── planner.py       # Task decomposition agent
│   ├── executor.py      # Task execution agent
│   └── reviewer.py      # Output validation agent
├── api/
│   └── server.py        # FastAPI REST server
├── examples/
│   └── demo_task.py     # Demo workflow script
├── requirements.txt
├── LICENSE
└── README.md
```

## ▶️ Quick Start

```bash
git clone https://github.com/fanyihuai26-dotcom/mimo-agent-hub.git
cd mimo-agent-hub
pip install -r requirements.txt

# Set your MiMo API key
export MIMO_API_KEY="your-api-key"

# Start the server
python api/server.py
```

Server runs at `http://localhost:8000` — visit `/docs` for the interactive API documentation.

### API Endpoints

| Method | Path | Description |
|---|---|---|
| `GET` | `/` | Health check & info |
| `POST` | `/plan` | Create an execution plan |
| `POST` | `/execute` | Full pipeline: plan → execute → review |
| `POST` | `/execute/step` | Execute a single step |
| `POST` | `/replan` | Adjust plan based on reviewer feedback |

### Example Request

```bash
curl -X POST http://localhost:8000/execute \
  -H "Content-Type: application/json" \
  -d '{"task": "Build a simple todo app with FastAPI backend"}'
```

## 🚧 Current Status

- ✅ Core agent pipeline (Planner → Executor → Reviewer)
- ✅ REST API with full CRUD endpoints
- ✅ Iterative replan loop
- 🔄 MiMo API integration (in progress)
- 📌 Next: Web UI dashboard + workflow visualization

## 🗺️ Roadmap

- [ ] Multi-agent memory & context persistence
- [ ] Web UI dashboard for task monitoring
- [ ] Plugin ecosystem for custom agent types
- [ ] Docker Compose deployment
- [ ] LangChain integration for advanced orchestration
- [ ] Open-source community & contribution guidelines

## 🤝 Contribution

Open to collaboration! Feel free to submit issues or pull requests.

## 📜 License

MIT License
