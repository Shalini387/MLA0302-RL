import pandas as pd

file_path = r"C:\Users\DELL\Downloads\RL_Experiments_11_to_20_Datasets\Exp11_StockTrading.csv"

data = pd.read_csv(file_path)

print("Stock Trading Dataset\n")
print(data)

states = data["State"].tolist()
actions = data["Action"].tolist()
rewards = data["Reward"].tolist()

learning_rate = 0.1
gamma = 0.9

online_q = [0] * len(states)
target_q = [0] * len(states)

print("\nTraining Double DQN\n")

for episode in range(10):

    for i in range(len(states)):

        target = rewards[i] + gamma * target_q[i]

        online_q[i] = online_q[i] + learning_rate * (target - online_q[i])

    target_q = online_q.copy()

print("Final Q Values\n")

for i in range(len(states)):
    print("State :", states[i])
    print("Action:", actions[i])
    print("Reward:", rewards[i])
    print("Q Value:", round(online_q[i], 2))
    print()

best = online_q.index(max(online_q))

print("Best Trading Strategy :", actions[best])
print("Expected Profit :", rewards[best])