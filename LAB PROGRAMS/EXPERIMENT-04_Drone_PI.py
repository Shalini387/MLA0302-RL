import pandas as pd

file_path = r"C:\Users\DELL\Downloads\RL_Experiments_1_to_10_Datasets_ZIP\Exp4_DroneRoute.xlsx"

data = pd.read_excel(file_path)

print("Drone Route Dataset\n")
print(data)

gamma = 0.9

states = data["Location"].tolist()
rewards = data["Reward"].tolist()

policy = ["Right", "Right", "Down", "Right", "Stop"]

values = [0] * len(states)

values[-1] = rewards[-1]

for i in range(len(states) - 2, -1, -1):
    values[i] = rewards[i] + gamma * values[i + 1]

print("\nOptimal Policy\n")

for i in range(len(states)):
    print("State :", states[i])

    if i < len(policy):
        print("Action:", policy[i])

    print("Reward:", rewards[i])
    print("Value :", round(values[i], 2))
    print()

print("Optimal Route")

for i in range(len(states)):
    if i < len(policy):
        print(states[i], "->", policy[i])