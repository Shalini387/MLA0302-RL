import pandas as pd

file_path = r"C:\Users\DELL\Downloads\RL_Experiments_1_to_10_Datasets_ZIP\Exp8_AutonomousCar.xlsx"

data = pd.read_excel(file_path)

print("Autonomous Car Dataset\n")
print(data)

gamma = 0.9

states = data["State"].tolist()
actions = data["Action"].tolist()
rewards = data["Reward"].tolist()

values = [0] * len(states)

values[-1] = rewards[-1]

for i in range(len(states) - 2, -1, -1):
    values[i] = rewards[i] + gamma * values[i + 1]

print("\nAutonomous Car Policy Evaluation\n")

for i in range(len(states)):
    print("State :", states[i])
    print("Action:", actions[i])
    print("Reward:", rewards[i])
    print("Value :", round(values[i], 2))
    print()

print("Navigation Policy")

for i in range(len(states)):
    print(states[i], "->", actions[i])

print("\nPolicy Effectiveness")

if values[0] > 10:
    print("The policy safely reaches the destination with high reward.")
else:
    print("The policy needs improvement.")