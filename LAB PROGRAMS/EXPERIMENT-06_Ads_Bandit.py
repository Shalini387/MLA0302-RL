import pandas as pd
import random

file_path = r"C:\Users\DELL\Downloads\RL_Experiments_1_to_10_Datasets_ZIP\Exp6_Advertisements.xlsx"

data = pd.read_excel(file_path)

print("Advertisement Dataset\n")
print(data)

ads = data["Ad_ID"].tolist()
ctr = data["CTR"].tolist()
rewards = data["Reward"].tolist()

epsilon = 0.2

epsilon_clicks = 0
ucb_clicks = 0
thompson_clicks = 0

print("\nEpsilon-Greedy Algorithm")

for i in range(len(ads)):

    if random.random() < epsilon:
        ad = random.randint(0, len(ads) - 1)
    else:
        ad = rewards.index(max(rewards))

    epsilon_clicks += rewards[ad]

print("Total Clicks =", epsilon_clicks)

print("\nUCB Algorithm")

best_ad = rewards.index(max(rewards))

for i in range(len(ads)):
    ucb_clicks += rewards[best_ad]

print("Total Clicks =", ucb_clicks)

print("\nThompson Sampling Algorithm")

for i in range(len(ads)):
    ad = random.randint(0, len(ads) - 1)
    thompson_clicks += rewards[ad]

print("Total Clicks =", thompson_clicks)

print("\nComparison")

print("Epsilon-Greedy :", epsilon_clicks)
print("UCB            :", ucb_clicks)
print("Thompson       :", thompson_clicks)

if epsilon_clicks >= ucb_clicks and epsilon_clicks >= thompson_clicks:
    print("\nBest Algorithm : Epsilon-Greedy")

elif ucb_clicks >= epsilon_clicks and ucb_clicks >= thompson_clicks:
    print("\nBest Algorithm : UCB")

else:
    print("\nBest Algorithm : Thompson Sampling")