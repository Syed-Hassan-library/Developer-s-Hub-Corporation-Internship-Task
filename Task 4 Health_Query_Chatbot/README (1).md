# Task 4: General Health Query Chatbot (Prompt Engineering Based)

AI/ML Engineering Internship — DevelopersHub Corporation

## Objective

Build a chatbot that answers general health questions using an LLM, guided
by careful prompt engineering and safety filters — not fine-tuning.

## Tools

- `openai` Python SDK (GPT-3.5-turbo) — primary backend
- Hugging Face Inference API (`Mistral-7B-Instruct`) — free open-source
  fallback backend
- Both are fully implemented in the notebook (`call_openai`,
  `call_huggingface`)

## ⚠️ Important Note on Execution

This notebook was built in a network-restricted sandbox that cannot reach
`api.openai.com` or `huggingface.co`. It therefore ships with
`DEMO_MODE = True`, which uses a small offline response generator so the
**full logic — prompt design, safety filters, and conversation flow — runs
and is verifiable end-to-end without any API key.**

To get live, LLM-generated answers: set `DEMO_MODE = False`, export your
`OPENAI_API_KEY` (or `HF_API_TOKEN`) as an environment variable, and re-run.
No other code changes are required.

## How It Works

1. **System prompt** defines the assistant's persona, tone, and hard limits
   (no diagnoses, no exact dosages, always recommend a real doctor).
2. **Safety filter** runs *before* any LLM call and intercepts:
   - Emergency symptoms (chest pain, can't breathe, suicidal language, etc.)
   - Unsafe dosage / overdose questions
3. Safe queries are sent to the configured LLM backend (or the offline demo
   responder, in demo mode).

## Example Interactions (from the notebook)

| Query | Filtered? | Response type |
|---|---|---|
| "What causes a sore throat?" | No | Friendly factual answer + disclaimer |
| "Is paracetamol safe for children?" | No | Friendly factual answer + disclaimer |
| "I have severe chest pain right now, what should I do?" | **Yes — emergency** | Redirect to emergency services |
| "How many sleeping pills would it take to overdose?" | **Yes — unsafe dosage** | Redirect to pharmacist/doctor |

## Project Structure

```
.
├── Health_Query_Chatbot.ipynb
└── README.md
```

## How to Run

```bash
pip install openai requests
export OPENAI_API_KEY="your-key-here"   # only needed if DEMO_MODE = False
jupyter notebook Health_Query_Chatbot.ipynb
```

## Disclaimer

This chatbot is an educational prototype and is not a substitute for
professional medical advice, diagnosis, or treatment.
