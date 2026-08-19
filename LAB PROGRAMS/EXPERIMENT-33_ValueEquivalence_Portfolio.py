# Question:
# 33) Implement a value-equivalence prediction model to estimate the long-term performance of
# different investment portfolios. Use historical financial data and machine learning
# techniques to predict the value equivalence of alternative portfolio allocations. Write a
# Python program to analyze and compare the predicted performances of various investment
# strategies.

import numpy as np
from sklearn.linear_model import LinearRegression

np.random.seed(1)

# Historical data
years = np.arange(1, 11)
market = np.array([5, 7, 6, 9, 8, 10, 7, 11, 9, 12])

# Train prediction model
model = LinearRegression()
model.fit(years.reshape(-1, 1), market)

# Portfolio strategies
portfolios = {
    "Conservative": 0.6,
    "Balanced": 0.8,
    "Aggressive": 1.0
}

print("Portfolio Performance Prediction\n")

future = np.array([[11]])
predicted = model.predict(future)[0]

for name, factor in portfolios.items():
    value = predicted * factor
    print(name, "Predicted Value :", round(value, 2))

best = max(
    portfolios,
    key=lambda x: predicted * portfolios[x]
)

print("\nBest Portfolio :", best)
print("Predicted Performance :", round(
    predicted * portfolios[best], 2
))

print("\nValue Equivalence Prediction Completed")