import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load the data
df = pd.read_csv("assets/all_stocks_5yr.csv")
stock = df[df["Name"] == "AAPL"].copy()
stock = stock.sort_values("date")

#predicting closing price
stock["next_close"] = stock["close"].shift(-1)
stock = stock.dropna()

X = stock[["close"]]
y = stock["next_close"]

#80|20 data split
split = int(len(stock) * 0.8)
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

#training model
model = LinearRegression()
model.fit(X_train, y_train)

#predictions
predictions = model.predict(X_test)

print("Mean Absolute Error:", mean_absolute_error(y_test, predictions))
print("R-squared:", r2_score(y_test, predictions))
print("Actual next close:", list(y_test.head(5)))
print("Predicted next close:", list(predictions[:5]))
