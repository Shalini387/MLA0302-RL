# Question:
# 24) In an inventory management system, use Bellman’s equation to find the optimal policy for
# ordering stock. Implement this in Python and demonstrate how the optimal policy minimizes costs.

import numpy as np

states = ["Low Stock", "Medium Stock", "High Stock"]
orders = [0, 5, 10]

cost = [10, 6, 3]
gamma = 0.9

value = np.zeros(3)

for _ in range(100):
    new_value = np.zeros(3)

    for i in range(3):
        values = [cost[i] + gamma * value[j] for j in range(3)]
        new_value[i] = min(values)

    value = new_value

print("Optimal Inventory Policy\n")

for i in range(3):
    values = [cost[i] + gamma * value[j] for j in range(3)]
    best = np.argmin(values)

    print("State :", states[i])
    print("Order :", orders[best], "units")
    print("Cost  :", round(values[best], 2))
    print()

print("Optimal policy minimizes inventory cost.")