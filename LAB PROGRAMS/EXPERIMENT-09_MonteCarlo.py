import pandas as pd
import random

file_path = r"C:\Users\DELL\Downloads\RL_Experiments_1_to_10_Datasets_ZIP\Exp9_CallCenter.xlsx"

data = pd.read_excel(file_path)

print("Call Center Dataset\n")
print(data)

states = data["Representative"].tolist()
rewards = data["Reward"].tolist()

episodes = 100

returns = [0] * len(states)
visits = [0] * len(states)

for episode in range(episodes):

    state = random.randint(0, len(states) - 1)

    reward = rewards[state]

    returns[state] += reward
    visits[state] += 1

values = []

for i in range(len(states)):
    if visits[i] != 0:
        values.append(round(returns[i] / visits[i], 2))
    else:
        values.append(0)

print("\nMonte Carlo State Value Function\n")

for i in range(len(states)):
    print("Representative :", states[i])
    print("Reward         :", rewards[i])
    print("Visits         :", visits[i])
    print("Value Function :", values[i])
    print()

best = values.index(max(values))

print("Best Assignment Policy :", states[best])