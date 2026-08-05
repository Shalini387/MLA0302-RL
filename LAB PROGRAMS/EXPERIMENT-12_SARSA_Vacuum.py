import pandas as pd

file_path = r"C:\Users\DELL\Downloads\RL_Experiments_11_to_20_Datasets\Exp12_RobotVacuum.csv"

data = pd.read_csv(file_path)

print("Robot Vacuum Dataset\n")
print(data)

rooms = data["Room"].tolist()
actions = data["Action"].tolist()
rewards = data["Reward"].tolist()

learning_rate = 0.1
gamma = 0.9

q_values = [0] * len(rooms)

print("\nTraining using SARSA\n")

for episode in range(10):

    for i in range(len(rooms)):

        next_state = (i + 1) % len(rooms)

        q_values[i] = q_values[i] + learning_rate * (
            rewards[i] + gamma * q_values[next_state] - q_values[i]
        )

print("State Action Values\n")

for i in range(len(rooms)):
    print("Room   :", rooms[i])
    print("Action :", actions[i])
    print("Reward :", rewards[i])
    print("Q Value:", round(q_values[i], 2))
    print()

best = q_values.index(max(q_values))

print("Optimal Cleaning Policy :", actions[best])
print("Maximum Reward :", rewards[best])