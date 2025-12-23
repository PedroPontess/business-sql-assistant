# 🎵 Chinook AI Assistant (SQL Agent)

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/downloads/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg?logo=docker&logoColor=white)](https://www.docker.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32-FF4B4B.svg)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-v0.1-green)](https://python.langchain.com)
[![Groq](https://img.shields.io/badge/LLM-Llama_3_70B-purple)](https://groq.com)

An Enterprise-grade AI Agent that allows non-technical users to query a SQL database using natural language. Built with a focus on **security**, **accuracy**, and **modern software engineering practices**.

<!-- ## 🔴 Live Demo
**[Click here to access the App](YOUR_STREAMLIT_APP_LINK_HERE)** -->

---

## 🏗️ Architecture & Features

This project moves beyond simple "Chat with Data" tutorials by implementing production-ready safeguards.

**The Pipeline:**
`User Query` → `Streamlit UI` → `LangChain Agent` → `Llama 3 (Groq)` → `SQLite DB (Read-Only)`

### Key Engineering Highlights
* **🔒 Read-Only Security:** The database connection uses strict URI flags (`?mode=ro&uri=true`) to enforce read-only access at the engine level, preventing prompt injection attacks (e.g., `DROP TABLE`).
* **🐳 Containerized Deployment:** Fully dockerized application ensuring consistency across Dev, Test, and Production environments.
* **🧵 Thread-Safe Concurrency:** Implements `StaticPool` for the SQLite connection to prevent race conditions and threading errors in the Streamlit web environment.
* **🧠 Schema-Aware Prompting:** The agent is initialized with a specialized system prompt that defines exact table names, join paths, and business logic.

---

## 🛠️ Project Structure

The project follows a modular source layout standard in professional Python development:

```text
business-sql-assistant/
├── .github/
│   └── workflows/
│       └── ci-pipeline.yml   # GitHub Actions (CI/CD)
├── tests/
│   └── test_security.py      # Security Verification (Pytest)
├── .dockerignore             # Docker build optimization
├── .env                      # API Keys (Not in repo)
├── .python-version           # Pinned Python version (3.12)
├── Dockerfile                # Container blueprint
├── pyproject.toml            # Project definition
├── uv.lock                   # Exact dependency locking
├── requirements.txt          # Production Dependencies
├── data/
│   └── Chinook.db            # SQLite Database
└── src/
    ├── app.py                # Streamlit Web Interface
    ├── agent.py              # LLM & Agent Configuration
    ├── database.py           # Secure DB Connection Logic
    └── main.py               # CLI Entrypoint
```

---

## 💻 Local Installation

This project uses uv for blazing fast dependency management, but supports standard pip as well.

### Option A: 🐳 Docker (Recommended)
Guarantees the app runs exactly as intended, isolated from your system.
```bash
# 1. Build the image
docker build -t chinook-agent .

# 2. Run the container
# This injects your API Key securely at runtime
docker run -p 8501:8501 --env-file .env chinook-agent
```

### Option B: ⚡ Using uv (Local Dev)
If you want to modify the code.
```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/business-sql-assistant.git
cd business-sql-assistant

# 2. Sync dependencies
uv sync

# 3. Run
uv run streamlit run src/app.py
```

### Option C: 🐍 Standard pip
Legacy support for systems without uv.
```bash
# 1. Create virtual env
python -m venv .venv
# Windows
.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate

# 2. Install requirements
pip install -r requirements.txt

# 3. Run the app
streamlit run src/app.py
```

---

## ⚙️ Configuration
1. Create a .env file in the root directory.
2. Add your Groq API Key:
```bash
GROQ_API_KEY=gsk_your_api_key_here
```

---

## 📜 License
This project is open-source and available under the MIT License.
