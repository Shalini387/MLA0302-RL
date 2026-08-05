import pandas as pd

file_path = r"C:\Users\DELL\Downloads\RL_Experiments_11_to_20_Datasets\Exp13_PacmanGrid.csv"

data = pd.read_csv(file_path)

print("Pac-Man Grid Dataset\n")
print(data)

states = data["State"].tolist()
actions = data["Action"].tolist()
rewards = data["Reward"].tolist()

learning_rate = 0.1
gamma = 0.9

q_table = [0] * len(states)

print("\nTraining using Q-Learning\n")

for episode in range(10):

    for i in range(len(states)):

        next_state = min(i + 1, len(states) - 1)

        q_table[i] = q_table[i] + learning_rate * (
            rewards[i] + gamma * q_table[next_state] - q_table[i]
        )

print("Q-Table\n")

for i in range(len(states)):
    print("State   :", states[i])
    print("Action  :", actions[i])
    print("Reward  :", rewards[i])
    print("Q Value :", round(q_table[i], 2))
    print()

best = q_table.index(max(q_table))

print("Best Action :", actions[best])
print("Maximum Reward :", rewards[best])