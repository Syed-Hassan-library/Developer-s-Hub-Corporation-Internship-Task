# Task 1: Exploring and Visualizing a Simple Dataset

AI/ML Engineering Internship — DevelopersHub Corporation

## Objective

Learn how to load, inspect, and visualize a dataset to understand data
trends and distributions.

## Dataset

**Iris Dataset** — 150 samples, 3 species (setosa, versicolor, virginica),
4 numeric features (sepal/petal length & width). Local copy included as
`iris.csv`.

## What's Inside

- Data loading and inspection (`.shape`, `.head()`, `.info()`, `.describe()`)
- Scatter plot and full pairplot of feature relationships
- Histograms of each feature's distribution, split by species
- Box plots to identify outliers per species

## Key Findings

- **Petal length/width** separate the 3 species far better than sepal
  measurements.
- **Setosa** is almost perfectly linearly separable from the other two
  species on petal features alone.
- **Versicolor** and **virginica** overlap somewhat, particularly on sepal
  measurements.
- A few mild outliers appear in sepal width for setosa, but nothing extreme.

## Project Structure

```
.
├── Iris_Dataset_Exploration.ipynb
├── iris.csv
└── README.md
```

## How to Run

```bash
pip install pandas matplotlib seaborn jupyter
jupyter notebook Iris_Dataset_Exploration.ipynb
```
