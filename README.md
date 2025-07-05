# 🤖 AI Agent Chatbot with FastAPI

This is an interactive AI chatbot web app that allows users to query powerful LLMs such as **LLaMA 3 (Groq)**, with optional real-time **web search** integration using **Tavily**. The app is built with **FastAPI** as the backend and **Streamlit** as the frontend.

---


## 🚀 Features

- 💬 Chat with powerful language models (LLaMA 3 via Groq API)
- 🔍 Option to enable web search using Tavily
- 🔧 Switchable model interface
- ⚡ Fast and responsive UI with Streamlit
- 🛠️ Modular codebase with separate backend/frontend

---

## 🧠 Tech Stack

| Component    | Tech        |
|--------------|-------------|
| Frontend     | Streamlit   |
| Backend      | FastAPI     |
| LLMs         | Groq (LLaMA3), OpenAI (optional) |
| Web Search   | Tavily API  |
| Agent System | LangChain   |
| Env Manager  | dotenv      |
| Package Mgmt | Conda + pip |

---

## 🗂️ Project Structure
```bash
.
├── ai_agent/
│   ├── ai_agent.py         # Agent setup and invocation
│   ├── backend.py          # FastAPI backend
│   ├── frontend.py         # Streamlit UI
├── .env                    # API keys (not uploaded)
├── requirements.txt        # All required packages
├── README.md               # You're here!

```
## Project Phases and Python Commands

### Phase 1: Create AI Agent
```
python ai_agent.py
```

### Phase 2: Setup Backend with FastAPI
```
python backend.py
```

### Phase 3: Setup Frontend with Streamlit
```
python frontend.py
```

## IMPORTANT
### Make sure backend python script is running in a separate terminal
