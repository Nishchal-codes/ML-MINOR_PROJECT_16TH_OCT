# Stock Price Prediction Using Machine Learning

A machine learning minor project exploring stock-price prediction from historical market data using **Simple Linear Regression**.

## Overview

This project investigates whether a simple regression model can estimate stock closing prices from selected numerical features. It demonstrates a basic machine-learning workflow: loading data, inspecting and cleaning it, preparing features, training a model, and evaluating predictions.

> **Disclaimer:** This project is for educational purposes only. It is not financial advice and should not be used to make investment decisions.

## Objectives

- Load and inspect historical stock-market data.
- Handle missing values and prepare data for modelling.
- Implement Simple Linear Regression using Python and scikit-learn.
- Split data into training and testing sets.
- Evaluate predictions using Mean Absolute Error (MAE) and R².
- Compare actual and predicted closing prices.

## Dataset

The project uses a historical stock-price dataset downloaded from Kaggle.

| Column | Description |
|---|---|
| `date` | Date associated with the record |
| `open` | Opening price |
| `high` | Highest price recorded |
| `low` | Lowest price recorded |
| `close` | Closing price |
| `volume` | Number of shares traded |
| `Name` | Stock ticker/company identifier |

The inspected dataset contains **619,040 records** across **505 stock identifiers**. A small number of records have missing values in `open`, `high`, or `low`.

**Dataset source:** Add the original Kaggle dataset URL here.

## Technologies

- Python 3
- Pandas — data loading and preprocessing
- NumPy — numerical operations
- scikit-learn — model training and evaluation
- VS Code — development environment
- Matplotlib — visualisation, if used in the script

## Methodology

1. Load the CSV dataset into a Pandas DataFrame.
2. Inspect data types, missing values, and duplicate rows.
3. Convert `date` to a datetime type and handle missing values.
4. Use `close` as the prediction target. The input features should match those actually used in `stock_prediction.py`.
5. Split the data into training and testing subsets. The initial experiment used an 80:20 split.
6. Train a Simple Linear Regression model.
7. Generate predictions on the test set.
8. Evaluate results using MAE and R².

## Initial Results

| Metric | Reported value |
|---|---:|
| Mean Absolute Error (MAE) | `1.2989` |
| R² score | `0.9766` |

These are results from the initial experiment, not a guarantee of future performance. The exact feature selection and splitting method affect how these metrics should be interpreted. For stock time-series data, a chronological split is generally more appropriate for testing forecasts on future dates than a random split.

## Project Structure

Suggested structure (adjust names to match your actual files):

```text
stock-price-prediction/
├── README.md
├── stock_prediction.py
└── data/
    └── <dataset-file>.csv
```

Avoid committing a large dataset if its licence or repository size makes that inappropriate; link to the original dataset instead.

## How to Run

1. Install Python 3.
2. Open a terminal in the project directory.
3. Install the required packages:

   ```bash
   python -m pip install pandas numpy scikit-learn matplotlib
   ```

   If your script does not use Matplotlib, you can omit it.

4. Update the dataset path in `stock_prediction.py` to match your CSV location.
5. Run the script:

   ```bash
   python stock_prediction.py
   ```

The script should display the evaluation metrics and sample predictions, depending on its implementation.

## Limitations

- Simple Linear Regression assumes a linear relationship.
- Historical patterns do not guarantee future price movements.
- The model does not account for news, company fundamentals, or macroeconomic changes.
- Results depend on feature selection, data cleaning, and the train/test split.
- A high R² score alone does not establish reliable real-world forecasting ability.

## Possible Improvements

- Use a chronological train/test split and evaluate on later dates.
- Compare against a simple baseline, such as predicting the previous closing price.
- Explore lagged prices and rolling averages, ensuring features use only information available at prediction time.
- Compare with other algorithms after learning them.
- Plot actual and predicted closing prices over time.

## Author

- **Name:** NISHCHAL SAHU
- **Course:** BCA
- **Project:** Machine Learning Minor Project
- **Language:** Python

## Acknowledgements

- Kaggle, for the historical dataset.
- The open-source Python ecosystem, including Pandas, NumPy, and scikit-learn.
