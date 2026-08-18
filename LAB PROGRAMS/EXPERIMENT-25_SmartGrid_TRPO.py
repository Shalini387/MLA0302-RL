import pandas as pd
import numpy as np

file_path = r"C:\Users\DELL\Downloads\Exp25_SmartGrid_TRPO.csv"

data = pd.read_csv(file_path)

print("Smart Grid Dataset\n")
print(data)

states = data["State"].tolist()
demand = data["Demand"].tolist()
production = data["Production"].tolist()
cost = data["Cost"].tolist()

actions = ["Reduce", "Maintain", "Increase"]

policy = np.ones((len(data), 3)) / 3

learning_rate = 0.1

for episode in range(10):
    for i in range(len(data)):

        balance = production[i] - demand[i]
        reward = 10 - abs(balance) - cost[i]

        best = np.argmax(policy[i])

        policy[i][best] += learning_rate * reward
        policy[i] = np.maximum(policy[i], 0)
        policy[i] /= policy[i].sum()

print("\nOptimized Energy Management Policy\n")

for i in range(len(data)):

    best = np.argmax(policy[i])

    print("State      :", states[i])
    print("Demand     :", demand[i])
    print("Production :", production[i])
    print("Cost       :", cost[i])
    print("Best Action:", actions[best])
    print("Policy     :", np.round(policy[i], 2))
    print()

print("TRPO Optimization Completed")