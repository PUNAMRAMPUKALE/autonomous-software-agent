# Autonomous Software Engineering Agent

An autonomous software engineering workflow that integrates Jira, GitHub and Large Language Models to analyze repositories, retrieve relevant code, generate implementations and prepare repository patches.

---

# Architecture

```text
                    +----------------+
                    |     Jira       |
                    +-------+--------+
                            |
                            v
                    +----------------+
                    | Planner Agent  |
                    +-------+--------+
                            |
                            v
                    +----------------+
                    | GitHub Agent   |
                    +-------+--------+
                            |
                            v
                    +----------------------+
                    | Repository Analyzer  |
                    +-------+--------------+
                            |
                            v
                    +----------------------+
                    | Indexing Agent       |
                    +-------+--------------+
                            |
                            v
                    +----------------------+
                    | Repository Graph     |
                    +-------+--------------+
                            |
                            v
                    +----------------------+
                    | Retrieval Agent      |
                    +-------+--------------+
                            |
                            v
                    +----------------------+
                    | Developer Agent      |
                    +-------+--------------+
                            |
                            v
                    +----------------------+
                    | Coding Agent         |
                    +-------+--------------+
                            |
                            v
                    +----------------------+
                    | LLM Provider         |
                    +-------+--------------+
                            |
                            v
                    +----------------------+
                    | Response Parser      |
                    +-------+--------------+
                            |
                            v
                    +----------------------+
                    | Patch Agent          |
                    +-------+--------------+
                            |
                            v
                    +----------------------+
                    | Patch Validator      |
                    +-------+--------------+
                            |
                            v
                    +----------------------+
                    | File Writer          |
                    +-------+--------------+
                            |
                            v
                    +----------------------+
                    | Repository           |
                    +----------------------+
```

---

# Features

- Jira integration
- GitHub repository management
- Repository analysis
- Symbol indexing
- Repository graph generation
- Intelligent code retrieval
- Impact analysis
- Developer context generation
- LLM abstraction layer
- Claude support
- OpenAI support
- Gemini support
- Ollama support
- Mock provider
- Patch generation
- Patch validation
- Safe file writing
- Rollback support

---

# Supported Providers

| Provider | Status |
|----------|--------|
| Mock | ✅ |
| Claude | ✅ |
| OpenAI | ✅ |
| Gemini | ✅ |
| Ollama | ✅ |

---

# Installation

```bash
python -m venv .venv

source .venv/bin/activate
```

Windows

```powershell
.\.venv\Scripts\Activate.ps1
```

Install packages

```bash
pip install -r requirements.txt
```

---

# Environment

Copy

```
.env.example
```

to

```
.env
```

Configure

- Jira
- GitHub
- LLM Provider

---

# Run

```bash
python app.py
```

---

# Workflow

1. Read Jira Story
2. Clone Repository
3. Analyze Repository
4. Build Repository Index
5. Build Repository Graph
6. Retrieve Relevant Symbols
7. Generate Developer Context
8. Generate Code
9. Parse LLM Response
10. Validate Patch
11. Apply Patch

---

# Project Structure

```
agents/
models/
tools/
workflow/
workspace/

app.py
config.py
requirements.txt
README.md
```

---

# Future Work

- Multi-agent planning
- AST-aware patch generation
- Automatic test execution
- Automatic pull request creation
- Slack notifications
- Code review agent
- Security analysis
- CI/CD integration
- Multi-language support

---

# License

MIT