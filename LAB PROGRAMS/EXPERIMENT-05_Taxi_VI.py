import pandas as pd

file_path = r"C:\Users\DELL\Downloads\RL_Experiments_1_to_10_Datasets_ZIP\Exp5_TaxiDispatch.xlsx"

data = pd.read_excel(file_path)

print("Taxi Dispatch Dataset\n")
print(data)

gamma = 0.9

states = data["Location"].tolist()
actions = data["Action"].tolist()
rewards = data["Reward"].tolist()

values = [0] * len(states)

values[-1] = rewards[-1]

for iteration in range(5):
    for i in range(len(states) - 2, -1, -1):
        values[i] = rewards[i] + gamma * values[i + 1]

print("\nOptimal Dispatch Policy\n")

for i in range(len(states)):
    print("State :", states[i])
    print("Action:", actions[i])
    print("Reward:", rewards[i])
    print("Value :", round(values[i], 2))
    print()

print("Optimal Route")

for i in range(len(states)):
    print(states[i], "->", actions[i])