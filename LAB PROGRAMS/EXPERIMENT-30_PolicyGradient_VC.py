# Question:
# 30) Train a virtual character to create engaging content (e.g., storytelling, interactive
# experiences) within a simulated virtual world using policy gradient methods. Implement the
# policy gradient algorithm in Python to optimize the character's behavior for maximum engagement.

import numpy as np

actions = ["Storytelling", "Interactive Game", "Explore", "Chat"]
rewards = [10, 9, 6, 7]

policy = np.ones(4) / 4
learning_rate = 0.1

for episode in range(20):

    action = np.random.choice(4, p=policy)
    reward = rewards[action]

    policy[action] += learning_rate * reward
    policy = policy / policy.sum()

    print("Episode", episode + 1,
          "Action:", actions[action],
          "Reward:", reward)

best = np.argmax(policy)

print("\nLearned Virtual Character Policy")

for i in range(4):
    print(actions[i], ":", round(policy[i], 2))

print("\nBest Behavior :", actions[best])
print("Maximum Engagement :", rewards[best])

print("\nPolicy Gradient Training Completed")