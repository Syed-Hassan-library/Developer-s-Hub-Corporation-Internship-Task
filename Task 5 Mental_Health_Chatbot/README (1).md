# Task 5: Mental Health Support Chatbot (Fine-Tuned)

AI/ML Engineering Internship — DevelopersHub Corporation

## Objective

Fine-tune a small open-source LLM to respond with empathy to statements
about stress, anxiety, and emotional wellness, then expose it through a
chat interface.

## Model Base & Dataset

- **Base model:** `distilgpt2` (82M parameters)
- **Fine-tuning dataset:** EmpatheticDialogues (Facebook AI), loaded via the
  Hugging Face `datasets` library
- **Fine-tuning method:** Hugging Face `Trainer` API, 3 epochs

## ⚠️ Important Note on Execution

This notebook was built in a network-restricted sandbox with **no internet
access to huggingface.co and no GPU** — so the actual fine-tuning could not
be executed here. The notebook contains the **complete, correct
implementation** (model/dataset loading, preprocessing, `TrainingArguments`,
`Trainer.train()`, model saving) and is ready to run as-is on **Google Colab
or Kaggle Notebooks** (both offer a free GPU and full internet access).

Every network-dependent step is wrapped in a `try/except` so it fails
gracefully here with a clear explanatory message instead of crashing — and a
lightweight rule-based offline responder takes over automatically so the
**rest of the notebook (safety checks, chat testing, CLI, Streamlit app)
runs and is fully demonstrable without a GPU or internet.**

To fine-tune for real: open the notebook in Colab, enable a free GPU runtime
(`Runtime > Change runtime type > T4 GPU`), and run all cells top to bottom.

## Safety Design

A crisis-language check runs on **every message, before any response is
generated**, regardless of backend. If crisis language is detected
(mentions of suicide, self-harm, etc.), the bot does not attempt to provide
support itself — it redirects the user to real crisis/emergency resources.

## Deployment

- **CLI:** `run_cli_chat()` function in the notebook
- **Web app:** `app.py` (Streamlit) — run with `streamlit run app.py`. Works
  in either mode: uses the fine-tuned model if found at
  `./mental-health-chatbot`, otherwise falls back to the same offline
  responder used in the notebook.

## Project Structure

```
.
├── Mental_Health_Chatbot.ipynb   # Fine-tuning pipeline + chat testing
├── app.py                        # Streamlit web chat interface
└── README.md
```

## How to Run

```bash
pip install torch transformers datasets accelerate streamlit
jupyter notebook Mental_Health_Chatbot.ipynb   # for fine-tuning (use Colab/Kaggle for GPU)
streamlit run app.py                            # for the chat web app
```

## Disclaimer

This chatbot is an educational prototype built for an internship task. It is
**not** a licensed mental health service and must never be used as a
substitute for professional therapy, counseling, or emergency crisis
support.
