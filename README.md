# 🤖 AI-Powered Chat Assistant (Panaversity Support Agent)

This is a smart, real-time AI chat assistant built using **Python**, **Chainlit**, and **Gemini API**. The agent can respond to user queries with streaming responses just like ChatGPT! ⚡

---

## 🔧 Features

- 🌐 Real-time AI conversation using Chainlit
- 🔄 Streamed responses (token by token)
- 🤝 Keeps chat history during the session
- 🤖 Integrated with Gemini-1.5 model (via OpenAI-like structure)
- 🔐 Uses `dotenv` for secure API key management

---

## 📦 Tech Stack

- **Python 3.10+**
- **Chainlit**
- **Gemini-1.5 Flash API** (Google)
- **OpenAI-compatible agent tools**
- **Dotenv** for environment variables

---

## 🚀 How to Run

1. **Clone the repository**

```bash
git clone https://github.com/uzmahmed26/Ai_Agent_with_chainlit.git
cd ai-chat-assistant
pip install -r requirements.txt
GEMINI_API_KEY=your_api_key_here
chainlit run main.py

