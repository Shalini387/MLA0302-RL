import pandas as pd

file_path = r"C:\Users\DELL\Downloads\RL_Experiments_11_to_20_Datasets\Exp14_GridWorld.csv"

data = pd.read_csv(file_path)

print("GridWorld Dataset\n")
print(data)

states = data["State"].tolist()
rewards = data["Reward"].tolist()

gamma = 0.9

values = [0] * len(states)

values[-1] = rewards[-1]

print("\nPolicy Iteration\n")

for iteration in range(5):

    for i in range(len(states)-2, -1, -1):

        values[i] = rewards[i] + gamma * values[i+1]

print("Optimal State Values\n")

for i in range(len(states)):
    print("State :", states[i])
    print("Reward:", rewards[i])
    print("Value :", round(values[i],2))
    print()

print("Optimal Policy\n")

for i in range(len(states)-1):

    if rewards[i] < 0:
        print(states[i], "-> Avoid Obstacle")
    else:
        print(states[i], "-> Move Forward")

print(states[-1], "-> Goal Reached")