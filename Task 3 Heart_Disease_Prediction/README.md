# Task 3: Heart Disease Prediction

AI/ML Engineering Internship — DevelopersHub Corporation

## Objective

Build a machine learning model that predicts whether a patient is at risk of
heart disease based on clinical features such as age, blood pressure,
cholesterol, and ECG results.

## Dataset

**Heart Disease UCI Dataset** (Cleveland Clinic dataset, 303 patient records,
13 features + 1 target). A local copy is included as `heart_disease.csv`.
The same dataset is publicly mirrored on Kaggle as *"Heart Disease UCI"*.

| Column | Meaning |
|---|---|
| age | Age in years |
| sex | 1 = male, 0 = female |
| cp | Chest pain type (0–3) |
| trestbps | Resting blood pressure (mm Hg) |
| chol | Serum cholesterol (mg/dl) |
| fbs | Fasting blood sugar > 120 mg/dl |
| restecg | Resting ECG results (0–2) |
| thalach | Maximum heart rate achieved |
| exang | Exercise induced angina |
| oldpeak | ST depression induced by exercise |
| slope | Slope of the peak exercise ST segment |
| ca | Number of major vessels (0–3) |
| thal | Thalassemia type (0–3) |
| target | 1 = heart disease present, 0 = no heart disease |

## Models Applied

- **Logistic Regression** (with feature scaling via `StandardScaler`)
- **Decision Tree Classifier** (`max_depth=4` to control overfitting)

## Key Results

| Model | Accuracy | ROC-AUC |
|---|---|---|
| Logistic Regression | ~0.85–0.90 | ~0.90+ |
| Decision Tree | ~0.78–0.85 | ~0.85+ |

*(Exact values are in the notebook output — they can vary slightly with the
random train/test split.)*

The most influential features across both models were **chest pain type
(cp)**, **number of major vessels (ca)**, **thalassemia (thal)**, **maximum
heart rate (thalach)**, and **ST depression (oldpeak)**.

## Project Structure

```
.
├── Heart_Disease_Prediction.ipynb   # Full notebook: EDA, training, evaluation
├── heart_disease.csv                # Dataset used
└── README.md
```

## How to Run

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
jupyter notebook Heart_Disease_Prediction.ipynb
```

## Disclaimer

This project is for educational purposes only as part of an AI/ML internship
task. It is **not** a certified medical tool and must not be used for real
clinical decision-making.
