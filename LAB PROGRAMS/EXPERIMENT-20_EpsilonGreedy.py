import pandas as pd
import random

file_path = r"C:\Users\DELL\Downloads\RL_Experiments_11_to_20_Datasets\Exp20_ContentRecommendation.csv"

data = pd.read_csv(file_path)

print("Content Recommendation Dataset\n")
print(data)

content = data["Content"]
clicks = data["Clicks"]
rewards = data["Reward"]

epsilon = 0.1
total_reward = 0
selected = [0] * len(content)

runs = 100

for _ in range(runs):

    if random.random() < epsilon:
        action = random.randint(0, len(content) - 1)
    else:
        action = rewards.tolist().index(max(rewards))

    total_reward += rewards[action]
    selected[action] += 1

print("\nEpsilon-Greedy Results\n")

for i in range(len(content)):
    print("Content   :", content[i])
    print("Clicks    :", clicks[i])
    print("Reward    :", rewards[i])
    print("Selected  :", selected[i])
    print()

best = selected.index(max(selected))

print("Best Content :", content[best])
print("Total Reward :", total_reward)