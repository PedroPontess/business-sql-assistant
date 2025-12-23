# 🎵 Chinook AI Assistant (SQL Agent)

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
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
* **🧵 Thread-Safe Concurrency:** Implements `StaticPool` for the SQLite connection to prevent race conditions and threading errors in the Streamlit web environment.
* **🧠 Schema-Aware Prompting:** The agent is initialized with a specialized system prompt that defines exact table names, join paths, and business logic (e.g., "Revenue comes from the Invoice table, not Track").
* **🔄 Self-Correction:** The Agent handles parsing errors gracefully, allowing the LLM to "retry" malformed SQL queries automatically.

---

## 🛠️ Project Structure

The project follows a modular source layout standard in professional Python development:

```text
business-sql-assistant/
├── .env                # API Keys (Not in repo)
├── pyproject.toml      # Dependency Management (uv)
├── requirements.txt    # Production Dependencies
├── data/
│   └── Chinook.db      # SQLite Database
└── src/
    ├── app.py          # Streamlit Web Interface
    ├── agent.py        # LLM & Agent Configuration
    ├── database.py     # Secure DB Connection Logic
    └── main.py         # CLI Entrypoint (Terminal mode)
```

---

## 💻 Local Installation

This project uses uv for blazing fast dependency management, but supports standard pip as well.

### Option A: Using uv (Recommended)
```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/business-sql-assistant.git
cd business-sql-assistant

# 2. Install dependencies and run
uv run streamlit run src/app.py
```

### Option B: Standard pip
```bash
# 1. Create virtual env
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

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
