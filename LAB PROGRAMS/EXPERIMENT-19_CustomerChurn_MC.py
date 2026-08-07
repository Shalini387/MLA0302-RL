import pandas as pd
import random

file_path = r"C:\Users\DELL\Downloads\RL_Experiments_11_to_20_Datasets\Exp19_CustomerChurn.csv"

data = pd.read_csv(file_path)

print("Customer Churn Dataset\n")
print(data)

customers = data["Customer"]
churn = data["Churn"]
rewards = data["Reward"]

returns = [0] * len(customers)
visits = [0] * len(customers)

episodes = 100

for _ in range(episodes):

    state = random.randint(0, len(customers) - 1)

    returns[state] += rewards[state]
    visits[state] += 1

values = []

for i in range(len(customers)):
    if visits[i] != 0:
        values.append(round(returns[i] / visits[i], 2))
    else:
        values.append(0)

print("\nPolicy Evaluation\n")

for i in range(len(customers)):
    print("Customer      :", customers[i])
    print("Churn Status  :", churn[i])
    print("Reward        :", rewards[i])
    print("Visits        :", visits[i])
    print("Value Function:", values[i])
    print()

best = values.index(max(values))

print("Best Customer Policy :", customers[best])
print("Maximum Reward :", rewards[best])