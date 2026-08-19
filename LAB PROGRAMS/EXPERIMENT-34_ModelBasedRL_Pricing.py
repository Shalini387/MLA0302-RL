# Question:
# 34) A dynamic pricing platform aims to optimize its pricing strategy using model-based RL.
# Develop a predictive model that forecasts customer demand and price sensitivities based on
# historical sales data. Use Python to train the predictive model and implement a model-based
# policy optimization algorithm to dynamically adjust prices.

import numpy as np
from sklearn.linear_model import LinearRegression

# Historical sales data
price = np.array([10, 15, 20, 25, 30, 35, 40])
demand = np.array([95, 85, 75, 65, 55, 45, 35])

# Train demand prediction model
model = LinearRegression()
model.fit(price.reshape(-1, 1), demand)

# Possible prices
prices = np.array([10, 15, 20, 25, 30, 35, 40])

predicted = model.predict(prices.reshape(-1, 1))
revenue = prices * predicted

print("Dynamic Pricing Optimization\n")

for i in range(len(prices)):
    print("Price :", prices[i],
          "Predicted Demand :", round(predicted[i], 2),
          "Revenue :", round(revenue[i], 2))

best = np.argmax(revenue)

print("\nOptimal Price :", prices[best])
print("Predicted Demand :", round(predicted[best], 2))
print("Maximum Revenue :", round(revenue[best], 2))

print("\nModel-Based RL Pricing Completed")