import pandas as pd
import random

file_path = r"C:\Users\DELL\Downloads\RL_Experiments_1_to_10_Datasets_ZIP\Exp3_DynamicPricing.xlsx"

data = pd.read_excel(file_path)

print("Dynamic Pricing Dataset\n")
print(data)

prices = data["Price"].tolist()
revenues = data["Revenue"].tolist()

epsilon = 0.2

epsilon_reward = 0
ucb_reward = 0
thompson_reward = 0

print("\nEpsilon-Greedy Strategy")

for i in range(len(prices)):

    if random.random() < epsilon:
        arm = random.randint(0, len(prices) - 1)
    else:
        arm = revenues.index(max(revenues))

    epsilon_reward += revenues[arm]

print("Total Revenue =", epsilon_reward)

print("\nUCB Strategy")

best_arm = revenues.index(max(revenues))

for i in range(len(prices)):
    ucb_reward += revenues[best_arm]

print("Total Revenue =", ucb_reward)

print("\nThompson Sampling Strategy")

for i in range(len(prices)):
    arm = random.randint(0, len(prices) - 1)
    thompson_reward += revenues[arm]

print("Total Revenue =", thompson_reward)

print("\nComparison")

print("Epsilon-Greedy :", epsilon_reward)
print("UCB            :", ucb_reward)
print("Thompson       :", thompson_reward)

if epsilon_reward >= ucb_reward and epsilon_reward >= thompson_reward:
    print("\nBest Strategy : Epsilon-Greedy")

elif ucb_reward >= epsilon_reward and ucb_reward >= thompson_reward:
    print("\nBest Strategy : UCB")

else:
    print("\nBest Strategy : Thompson Sampling")