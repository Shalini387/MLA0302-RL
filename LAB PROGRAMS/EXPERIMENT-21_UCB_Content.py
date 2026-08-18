import numpy as np

content = ["Movie", "Series", "Sports", "Documentary", "Music"]
rewards = [10, 8, 7, 6, 5]

count = np.zeros(len(content))
total_reward = np.zeros(len(content))

rounds = 100

for t in range(rounds):

    if t < len(content):
        action = t
    else:
        average = total_reward / np.maximum(count, 1)
        confidence = np.sqrt(2 * np.log(t + 1) / np.maximum(count, 1))
        ucb = average + confidence
        action = np.argmax(ucb)

    count[action] += 1
    total_reward[action] += rewards[action]

print("UCB Results\n")

for i in range(len(content)):
    print("Content :", content[i])
    print("Selections :", int(count[i]))
    print("Average Reward :", round(total_reward[i] / count[i], 2))
    print()

best = np.argmax(total_reward)

print("Best Content :", content[best])
print("Total Reward :", int(total_reward.sum()))