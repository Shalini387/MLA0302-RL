# Question:
# 32) A retail company aims to optimize its inventory management strategy using model-based RL.
# Develop a data generation model that simulates customer demand patterns and inventory
# dynamics. Use Python to generate synthetic data and evaluate different inventory
# management policies based on the simulated environment.

import numpy as np

np.random.seed(1)

inventory = 50
days = 10

demand = np.random.randint(5, 16, days)

policies = {
    "Low Order": 5,
    "Medium Order": 10,
    "High Order": 15
}

print("Synthetic Demand:", demand)
print("\nInventory Policy Evaluation\n")

for name, order in policies.items():

    stock = inventory
    cost = 0

    for d in demand:
        stock += order
        stock -= min(stock, d)
        cost += stock + order * 0.5

    print(name)
    print("Order Quantity :", order)
    print("Total Cost :", round(cost, 2))
    print()

best = min(
    policies,
    key=lambda p: sum(
        inventory + policies[p] * 0.5
        for _ in demand
    )
)

print("Best Inventory Policy :", best)
print("Model-Based RL Evaluation Completed")