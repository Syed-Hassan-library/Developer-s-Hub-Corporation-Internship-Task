# Task 2: Predict Future Stock Prices (Short-Term)

AI/ML Engineering Internship — DevelopersHub Corporation

## Objective

Use historical stock data to predict closing price from a day's Open, High,
Low, and Volume.

## Stock & Dataset

**Apple Inc. (AAPL)** — 506 trading days of daily OHLCV data
(Feb 2015 – Feb 2017).

## ⚠️ Important Note on Data Source

The task suggests `yfinance` for live data, but this notebook's sandbox
network couldn't reach Yahoo Finance's servers, so a static historical CSV
with the identical Open/High/Low/Close/Volume structure was used instead.
The real `yfinance` download code is included (commented out) in Section 1
— uncomment and run it on a machine with normal internet access to fetch
live data for any ticker (Apple, Tesla, etc.).

## Models Applied

- **Linear Regression**
- **Random Forest Regressor** (`n_estimators=200`, `max_depth=6`)

## Key Results

| Model | MAE | RMSE | R² |
|---|---|---|---|
| Linear Regression | 0.371 | 0.517 | 0.9940 |
| Random Forest | 0.598 | 0.886 | 0.9823 |

## Key Findings

- Both models predict the same-day closing price very accurately, since
  `Open`/`High`/`Low` are naturally very close to `Close` on the same
  trading day — this is closer to interpolation than real forecasting.
- Linear Regression actually edges out Random Forest here because the
  same-day OHLC relationship is close to linear.
- **A genuinely fair next-day forecast** would need to use only information
  available *before* the next trading day (yesterday's data, technical
  indicators), not the next day's own High/Low — see the notebook's
  conclusion for a discussion of this.

## Project Structure

```
.
├── Stock_Price_Prediction.ipynb
├── apple_stock.csv
└── README.md
```

## How to Run

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter yfinance
jupyter notebook Stock_Price_Prediction.ipynb
```

## Disclaimer

This is an educational exercise, not financial advice.
