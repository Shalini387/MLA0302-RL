import pandas as pd

file_path = r"C:\Users\DELL\Downloads\RL_Experiments_11_to_20_Datasets\Exp16_BellmanRobot.csv"

data = pd.read_csv(file_path)

print("Robot Navigation Dataset\n")
print(data)

states = data["State"].tolist()
rewards = data["Reward"].tolist()

gamma = 0.9

values = [0] * len(states)

values[-1] = rewards[-1]

print("\nBellman Optimality Computation\n")

for iteration in range(5):

    for i in range(len(states)-2, -1, -1):

        values[i] = rewards[i] + gamma * values[i+1]

print("Optimal State Value Function\n")

for i in range(len(states)):
    print("State :", states[i])
    print("Reward:", rewards[i])
    print("Value :", round(values[i],2))
    print()

print("Optimal Path\n")

for i in range(len(states)-1):
    print(states[i], "->", states[i+1])

print("Goal Reached :", states[-1])