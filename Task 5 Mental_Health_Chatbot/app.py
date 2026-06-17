"""
Streamlit web interface for the Mental Health Support Chatbot (Task 5).

Run with:
    streamlit run app.py

Uses the same backend-agnostic response logic as the notebook:
- If a fine-tuned distilgpt2 model is available at MODEL_DIR, it is used.
- Otherwise, a lightweight rule-based offline responder is used instead,
  so this app runs out of the box with no GPU or internet required.

A crisis-language safety check always runs first, regardless of backend.
"""

import os
import re
import random

import streamlit as st

MODEL_DIR = "./mental-health-chatbot"

# ---------------------------------------------------------------------------
# Try to load the fine-tuned model (produced by the notebook's Section 4).
# Falls back gracefully if it isn't available.
# ---------------------------------------------------------------------------
MODEL_AVAILABLE = False
tokenizer = None
model = None

if os.path.isdir(MODEL_DIR):
    try:
        from transformers import AutoTokenizer, AutoModelForCausalLM

        tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
        model = AutoModelForCausalLM.from_pretrained(MODEL_DIR)
        MODEL_AVAILABLE = True
    except Exception:
        MODEL_AVAILABLE = False

# ---------------------------------------------------------------------------
# Crisis safety check (always runs, regardless of backend)
# ---------------------------------------------------------------------------
CRISIS_PATTERNS = [
    r"suicide", r"kill myself", r"end my life", r"want to die",
    r"self.?harm", r"hurt myself", r"no reason to live",
]

CRISIS_RESPONSE = (
    "I'm really glad you told me this, and I want to take it seriously: it sounds "
    "like you're going through something very heavy right now. I'm not able to "
    "give you the kind of support you need in this moment, but please reach out "
    "right now to a crisis line or emergency service in your area, or to someone "
    "you trust. You deserve real, immediate support — you don't have to carry this alone."
)


def is_crisis_message(text: str) -> bool:
    t = text.lower()
    return any(re.search(p, t) for p in CRISIS_PATTERNS)


# ---------------------------------------------------------------------------
# Offline rule-based fallback responder
# ---------------------------------------------------------------------------
_EMPATHETIC_TEMPLATES = {
    "stress":   ["That sounds like a lot to carry right now. What's weighing on you the most?",
                 "Stress like that is exhausting. Have you been able to take any breaks today?"],
    "anxious":  ["It makes sense to feel anxious about that — it matters to you. What's the part that worries you most?",
                 "Anxiety can be really overwhelming. Try taking a slow breath with me — what's on your mind?"],
    "anxiety":  ["It makes sense to feel anxious about that — it matters to you. What's the part that worries you most?"],
    "sad":      ["I'm sorry you're feeling this way. Do you want to tell me more about what's going on?",
                 "That sounds really hard. I'm here to listen, whenever you're ready."],
    "lonely":   ["Feeling lonely is genuinely painful, and I'm glad you reached out instead of sitting with it alone.",
                 "I hear you — feeling unseen by others is hard. I'm here, and I'm listening."],
    "tired":    ["It sounds like you're running on empty. Has it been like this for a while?"],
    "angry":    ["That frustration makes sense given what you described. What happened?"],
    "happy":    ["I love hearing that! Tell me more about what's making you feel good.",
                 "That's wonderful — thank you for sharing something good with me."],
    "great":    ["I love hearing that! Tell me more about what's making you feel good."],
    "excited":  ["That excitement is wonderful — what are you looking forward to most?"],
}


def offline_demo_response(user_text: str) -> str:
    t = user_text.lower()
    for keyword, templates in _EMPATHETIC_TEMPLATES.items():
        if keyword in t:
            return random.choice(templates)
    return "Thank you for sharing that with me. Can you tell me a little more about how you're feeling?"


def generate_with_finetuned_model(user_text: str, max_new_tokens: int = 60) -> str:
    prompt = f"Context: {user_text}\nResponse:"
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        **inputs, max_new_tokens=max_new_tokens, do_sample=True,
        top_p=0.9, temperature=0.8, pad_token_id=tokenizer.eos_token_id,
    )
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return decoded.split("Response:")[-1].strip()


def get_response(user_text: str) -> str:
    if is_crisis_message(user_text):
        return CRISIS_RESPONSE
    if MODEL_AVAILABLE:
        return generate_with_finetuned_model(user_text)
    return offline_demo_response(user_text)


# ---------------------------------------------------------------------------
# Streamlit UI
# ---------------------------------------------------------------------------
st.set_page_config(page_title="Mental Health Support Chatbot", page_icon="💬")
st.title("💬 Mental Health Support Chatbot")
st.caption(
    "An empathetic listening prototype — not a replacement for therapy or "
    "emergency support. " + ("Using the fine-tuned model." if MODEL_AVAILABLE
                              else "Running in offline demo mode (no fine-tuned model found).")
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Share what's on your mind...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    bot_reply = get_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.write(bot_reply)

st.divider()
st.caption(
    "If you are in crisis or thinking about harming yourself, please contact a "
    "local emergency number or crisis helpline right away."
)
