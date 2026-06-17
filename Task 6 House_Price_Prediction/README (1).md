# Task 6: House Price Prediction

AI/ML Engineering Internship — DevelopersHub Corporation

## Objective

Predict house prices using property features such as rooms, bedrooms,
income, and location.

## Dataset

**California Housing Prices Dataset** (20,640 district-level records,
1990 California census). Includes size-related features (rooms, bedrooms,
population, households) and location features (longitude/latitude,
ocean proximity). A local copy is included as `housing.csv`. This dataset
is the standard, widely-used stand-in for the Kaggle "House Price
Prediction Dataset" referenced in the task.

## Models Applied

- **Linear Regression** (baseline, with feature scaling)
- **Gradient Boosting Regressor** (`n_estimators=200`, `max_depth=3`)

## Key Results

| Model | MAE | RMSE | R² |
|---|---|---|---|
| Linear Regression | ~50,000 | ~70,000 | ~0.64 |
| Gradient Boosting | ~31,000 | ~48,000 | ~0.83 |

*(See the notebook for exact values.)*

Gradient Boosting clearly outperforms the linear baseline, since house
prices have non-linear relationships with income and location that a
straight-line model can't capture.

## Key Findings

- **Median income** is the single strongest predictor of house value.
- Location features (latitude/longitude, ocean proximity) are the next most
  important — confirming that "location, location, location" holds true in
  the data.
- Engineered ratio features (`rooms_per_household`, `bedrooms_per_room`)
  added more predictive power than the raw totals.

## Project Structure

```
.
├── House_Price_Prediction.ipynb   # Full notebook: EDA, training, evaluation
├── housing.csv                    # Dataset used
└── README.md
```

## How to Run

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
jupyter notebook House_Price_Prediction.ipynb
```
