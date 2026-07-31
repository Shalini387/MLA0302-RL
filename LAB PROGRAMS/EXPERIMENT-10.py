import random

actions = ["Buy", "Hold", "Sell"]

rewards = [10, 5, 2]

policy = [0.33, 0.33, 0.34]

learning_rate = 0.1

print("Initial Policy")
for i in range(len(actions)):
    print(actions[i], "=", round(policy[i], 2))

for episode in range(10):

    action = random.randint(0, 2)

    reward = rewards[action]

    policy[action] = policy[action] + learning_rate * reward / 100

total = sum(policy)

policy = [p / total for p in policy]

print("\nOptimized Policy")

for i in range(len(actions)):
    print(actions[i], "=", round(policy[i], 2))

best = policy.index(max(policy))

print("\nBest Investment Strategy:", actions[best])