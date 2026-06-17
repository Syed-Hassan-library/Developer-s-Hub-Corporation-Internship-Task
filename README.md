
# AI/ML Engineering Internship Tasks

**DevelopersHub Corporation — AI/ML Engineering Internship**

This repository contains my completed tasks for the AI/ML Engineering
Internship at DevelopersHub Corporation. All 6 tasks from the internship
brief have been completed (the requirement was a minimum of 3).

## Tasks

| # | Task | Folder | Description |
|---|---|---|---|
| 1 | Exploring and Visualizing a Simple Dataset | [`Task1_Iris_Dataset`](./Task1_Iris_Dataset) | EDA and visualization on the Iris dataset |
| 2 | Predict Future Stock Prices (Short-Term) | [`Task2_Stock_Prediction`](./Task2_Stock_Prediction) | Regression models to predict AAPL closing price |
| 3 | Heart Disease Prediction | [`Task3_Heart_Disease`](./Task3_Heart_Disease) | Classification models to predict heart disease risk |
| 4 | General Health Query Chatbot | [`Task4_Health_Chatbot`](./Task4_Health_Chatbot) | Prompt-engineered LLM chatbot with safety filters |
| 5 | Mental Health Support Chatbot (Fine-Tuned) | [`Task5_Mental_Health_Chatbot`](./Task5_Mental_Health_Chatbot) | Fine-tuning DistilGPT2 on EmpatheticDialogues |
| 6 | House Price Prediction | [`Task6_House_Price`](./Task6_House_Price) | Regression models to predict California housing prices |

Each folder contains its own notebook, dataset (where applicable), and a
README with the task's objective, dataset, models used, and key results.

## Skills Practiced

- Data loading, cleaning, and exploratory data analysis (EDA)
- Data visualization with `matplotlib` and `seaborn`
- Regression modeling (Linear Regression, Random Forest, Gradient Boosting)
- Classification modeling (Logistic Regression, Decision Tree) and
  evaluation (accuracy, ROC-AUC, confusion matrix)
- Prompt engineering and safety-filter design for LLM-based chatbots
- Fine-tuning a language model with the Hugging Face `Trainer` API
- Building simple CLI and Streamlit-based conversational interfaces

## How to Run

Each task folder has its own README with specific setup instructions.
In general:

```bash
git clone <this-repo-url>
cd <task-folder>
pip install -r requirements.txt   # or see the task's README for exact packages
jupyter notebook <notebook-name>.ipynb
```

## Author

Syed — AI & Data Science student, Saylani Mass IT Training, Karachi
