import streamlit as st
import ollama

st.set_page_config(page_title="💫 Nova Chat 💫", page_icon="💫", layout="centered")

st.html("""
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700;800&display=swap" rel="stylesheet"/>
<style>
/* ── Root & Body ── */
:root {
  --pink: #FF2D9B;
  --blue: #00CFFF;
  --dark: #1A1A2E;
  --pink-glow: rgba(255,45,155,0.45);
  --blue-glow: rgba(0,207,255,0.4);
}
html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
  background: var(--dark) !important;
  font-family: 'Space Grotesk', sans-serif !important;
}
[data-testid="stAppViewContainer"] {
  background:
    radial-gradient(ellipse at 20% 50%, rgba(255,45,155,0.08) 0%, transparent 60%),
    radial-gradient(ellipse at 80% 20%, rgba(0,207,255,0.08) 0%, transparent 60%),
    #1A1A2E !important;
}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header, [data-testid="stToolbar"],
[data-testid="stDecoration"], [data-testid="stStatusWidget"] { display: none !important; }

/* ── Title ── */
h1 {
  font-family: 'Space Grotesk', sans-serif !important;
  font-weight: 800 !important;
  font-size: 2rem !important;
  text-align: center !important;
  background: linear-gradient(90deg, var(--pink), #cc00ff, var(--blue));
  -webkit-background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
  background-clip: text !important;
  text-shadow: none !important;
  padding: 10px 0 4px !important;
  letter-spacing: 0.04em;
}

/* ── Chat messages container ── */
[data-testid="stChatMessageContainer"],
[data-testid="stChatMessage"] {
  background: transparent !important;
  border: none !important;
}

/* ── User message bubble ── */
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
  flex-direction: row-reverse !important;
}
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) [data-testid="stMarkdownContainer"] p,
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) .stMarkdown p {
  background: linear-gradient(135deg, #FF2D9B 0%, #ff80c8 100%) !important;
  color: white !important;
  padding: 11px 18px !important;
  border-radius: 20px 20px 5px 20px !important;
  display: inline-block !important;
  font-family: 'Space Grotesk', sans-serif !important;
  font-weight: 600 !important;
  font-size: 0.95rem !important;
  box-shadow: 4px 4px 0 #880055, 0 0 18px var(--pink-glow) !important;
  max-width: 75% !important;
  float: right !important;
  clear: both !important;
  position: relative !important;
}

/* ── AI message bubble ── */
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) [data-testid="stMarkdownContainer"] p,
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) .stMarkdown p {
  background: linear-gradient(135deg, #0090cc 0%, #00CFFF 100%) !important;
  color: white !important;
  padding: 11px 18px !important;
  border-radius: 20px 20px 20px 5px !important;
  display: inline-block !important;
  font-family: 'Space Grotesk', sans-serif !important;
  font-weight: 600 !important;
  font-size: 0.95rem !important;
  box-shadow: 4px 4px 0 #005577, 0 0 18px var(--blue-glow) !important;
  max-width: 75% !important;
  clear: both !important;
  position: relative !important;
}

/* ── Avatars ── */
[data-testid="chatAvatarIcon-user"] {
  background: linear-gradient(135deg, var(--pink), #cc00ff) !important;
  border: 2px solid white !important;
  box-shadow: 2px 2px 0 #1A1A2E !important;
}
[data-testid="chatAvatarIcon-assistant"] {
  background: linear-gradient(135deg, #0090cc, var(--blue)) !important;
  border: 2px solid white !important;
  box-shadow: 2px 2px 0 #1A1A2E !important;
}

/* ── Chat input ── */
[data-testid="stChatInput"] {
  border: 2.5px solid rgba(255,45,155,0.6) !important;
  border-radius: 999px !important;
  background: rgba(255,255,255,0.06) !important;
  font-family: 'Space Grotesk', sans-serif !important;
  font-weight: 600 !important;
  color: white !important;
  box-shadow: 0 0 16px var(--pink-glow) !important;
  padding: 10px 20px !important;
}
[data-testid="stChatInput"]:focus-within {
  border-color: var(--pink) !important;
  box-shadow: 0 0 0 3px var(--pink-glow), 0 0 24px var(--pink-glow) !important;
}
[data-testid="stChatInput"] textarea {
  color: white !important;
  font-family: 'Space Grotesk', sans-serif !important;
  font-weight: 600 !important;
  background: transparent !important;
}
[data-testid="stChatInput"] textarea::placeholder {
  color: rgba(255,255,255,0.35) !important;
}

/* ── Send button ── */
[data-testid="stChatInputSubmitButton"] button {
  background: linear-gradient(135deg, var(--pink), #cc00ff) !important;
  border-radius: 999px !important;
  border: none !important;
  box-shadow: 3px 3px 0 #880055, 0 0 14px var(--pink-glow) !important;
  color: white !important;
  font-weight: 800 !important;
}
[data-testid="stChatInputSubmitButton"] button:hover {
  transform: translateY(-2px) !important;
  box-shadow: 3px 5px 0 #880055, 0 0 22px var(--pink-glow) !important;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--pink); border-radius: 4px; }

/* ── Floating hearts animation ── */
@keyframes floatUp {
  0%   { transform: translateY(0) rotate(0deg); opacity: 0.5; }
  100% { transform: translateY(-100vh) rotate(20deg); opacity: 0; }
}
.heart {
  position: fixed;
  pointer-events: none;
  z-index: 0;
  font-size: 1.2rem;
  animation: floatUp linear infinite;
}
</style>

<!-- Floating hearts -->
<div class="heart" style="left:5vw;  animation-duration:9s;  animation-delay:0s;">♥</div>
<div class="heart" style="left:15vw; animation-duration:13s; animation-delay:2s;">★</div>
<div class="heart" style="left:25vw; animation-duration:8s;  animation-delay:5s;">✨</div>
<div class="heart" style="left:40vw; animation-duration:11s; animation-delay:1s;">💖</div>
<div class="heart" style="left:55vw; animation-duration:14s; animation-delay:3s;">⭐</div>
<div class="heart" style="left:70vw; animation-duration:9s;  animation-delay:7s;">♥</div>
<div class="heart" style="left:82vw; animation-duration:12s; animation-delay:4s;">★</div>
<div class="heart" style="left:92vw; animation-duration:10s; animation-delay:6s;">💫</div>
""")

st.title("💫 Nova Chat 💫")
st.html("<p style='text-align:center; color:rgba(255,255,255,0.4); font-family:Space Grotesk,sans-serif; font-size:0.8rem; margin-top:-12px; margin-bottom:16px;'>♥ powered by ollama ♥ running local ♥</p>")

# ── System prompt ──
SYSTEM_PROMPT = {
    "role": "system",
    "content": "You're Nova, a cool and witty AI. You're laid-back, occasionally sarcastic, drop clever one-liners, and never sound like a boring assistant. Keep answers concise and fun."
}

# ── Session state ──
if "messages" not in st.session_state:
    st.session_state.messages = []

# ── Display chat history ──
for message in st.session_state.messages:
    avatar = "💫" if message["role"] == "user" else "🤖"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# ── User input ──
if prompt := st.chat_input("type something cute... ♥"):

    with st.chat_message("user", avatar="💫"):
        st.markdown(prompt)

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant", avatar="🤖"):
        response_placeholder = st.empty()
        full_response = ""

        stream = ollama.chat(
            model="llama3",
            messages=[SYSTEM_PROMPT] + st.session_state.messages,
            stream=True
        )

        for chunk in stream:
            token = chunk["message"]["content"]
            full_response += token
            response_placeholder.markdown(full_response + "▌")

        response_placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})
