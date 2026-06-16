# 💫 Nova Chat

A retro Y2K-styled AI chatbot built with Streamlit and Ollama. Nova is your chill, witty local AI bestie — no API keys, no cloud, runs entirely on your machine.

---

## ✨ Features

- 💬 Streaming chat responses (token by token)
- 🎨 Y2K bubblegum aesthetic — pink & blue gradient bubbles, floating hearts, glowing input
- 🤖 Custom AI personality — laid-back, witty, and never boring
- 🔒 Fully local — powered by Ollama, no data leaves your machine
- 🧠 Multi-turn memory — maintains full conversation context

---

## 🛠️ Tech Stack

| Layer     | Tool                          |
|-----------|-------------------------------|
| Frontend  | Streamlit 1.58+               |
| AI Model  | Ollama (`llama3`)             |
| Styling   | Custom CSS via `st.html()`    |
| Font      | Space Grotesk (Google Fonts)  |

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://code.swecha.org/f20240032/chatbot.git
cd chatbot
```

### 2. Install dependencies

```bash
pip install streamlit ollama
```

### 3. Install and start Ollama

Download Ollama from [ollama.com](https://ollama.com) then run:

```bash
ollama pull llama3
ollama serve
```

### 4. Run the app

```bash
streamlit run streamlit-app.py
```

Open your browser at `http://localhost:8501`

---

## 📁 Project Structure

```
chatbot/
└── streamlit-app.py   # Main app — UI + chat logic
└── README.md
```

---

## ⚙️ Configuration

To change the model, edit this line in `streamlit-app.py`:

```python
model="llama3"  # swap with "mistral", "gemma3", etc.
```

To change Nova's personality, edit the `SYSTEM_PROMPT`:

```python
SYSTEM_PROMPT = {
    "role": "system",
    "content": "You're Nova..." # your custom vibe here
}
```

---

## 🖥️ Local Setup (Windows)

Make sure Ollama is running before starting Streamlit:

```cmd
ollama serve
```

Then in a separate terminal:

```cmd
streamlit run streamlit-app.py
```

---

## 📸 Preview

> Y2K pink & blue aesthetic with floating ♥ ★ 💫 animations, glossy chat bubbles, and a glowing input bar.

---

*Built with 💫 at swecha*
