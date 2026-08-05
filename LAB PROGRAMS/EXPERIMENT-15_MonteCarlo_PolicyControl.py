import pandas as pd
import random

file_path = r"C:\Users\DELL\Downloads\RL_Experiments_11_to_20_Datasets\Exp15_CallCenter_MC.csv"

data = pd.read_csv(file_path)

print("Call Center Dataset\n")
print(data)

representatives = data["Representative"].tolist()
call_time = data["Call_Time"].tolist()
rewards = data["Reward"].tolist()

episodes = 100

returns = [0] * len(representatives)
visits = [0] * len(representatives)

print("\nMonte Carlo Policy Control\n")

for episode in range(episodes):

    state = random.randint(0, len(representatives) - 1)

    reward = rewards[state]

    returns[state] += reward
    visits[state] += 1

values = []

for i in range(len(representatives)):
    if visits[i] != 0:
        values.append(round(returns[i] / visits[i], 2))
    else:
        values.append(0)

for i in range(len(representatives)):
    print("Representative :", representatives[i])
    print("Call Time      :", call_time[i])
    print("Reward         :", rewards[i])
    print("Visits         :", visits[i])
    print("Value Function :", values[i])
    print()

best = values.index(max(values))

print("Optimal Representative :", representatives[best])
print("Minimum Call Time :", call_time[best], "minutes")