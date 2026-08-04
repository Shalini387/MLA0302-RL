import pandas as pd
import matplotlib.pyplot as plt

file_path = r"C:\Users\DELL\Downloads\RL_Experiments_1_to_10_Datasets_ZIP\Exp7_DeliveryRobot.xlsx"

data = pd.read_excel(file_path)

print("Delivery Robot Dataset\n")
print(data)

gamma = 0.9

states = data["State"].tolist()
rewards = data["Reward"].tolist()

values = [0] * len(states)

values[-1] = rewards[-1]

for i in range(len(states) - 2, -1, -1):
    values[i] = rewards[i] + gamma * values[i + 1]

print("\nState Value Function\n")

for i in range(len(states)):
    print("State :", states[i])
    print("Reward:", rewards[i])
    print("Value :", round(values[i], 2))
    print()

plt.figure(figsize=(7,4))
plt.plot(states, values, marker='o')
plt.title("State Value Function")
plt.xlabel("States")
plt.ylabel("Value")
plt.grid(True)
plt.show()