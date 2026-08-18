import numpy as np

campaigns = ["Email", "Social Media", "Search Ads", "SMS"]
reward = [8, 6, 10, 5]
runs = 100
epsilon = 0.1

def epsilon_greedy():
    total = 0
    q = np.zeros(4)
    count = np.zeros(4)

    for _ in range(runs):
        i = np.random.randint(4) if np.random.rand() < epsilon else np.argmax(q)
        count[i] += 1
        q[i] += (reward[i] - q[i]) / count[i]
        total += reward[i]

    return total

def ucb():
    total = 0
    count = np.zeros(4)
    value = np.zeros(4)

    for t in range(runs):
        if t < 4:
            i = t
        else:
            ucb_value = value + np.sqrt(2 * np.log(t + 1) / count)
            i = np.argmax(ucb_value)

        count[i] += 1
        value[i] += (reward[i] - value[i]) / count[i]
        total += reward[i]

    return total

def thompson():
    total = 0
    alpha = np.ones(4)
    beta = np.ones(4)

    for _ in range(runs):
        samples = np.random.beta(alpha, beta)
        i = np.argmax(samples)
        total += reward[i]

        if reward[i] >= max(reward) * 0.8:
            alpha[i] += 1
        else:
            beta[i] += 1

    return total

eg = epsilon_greedy()
ucb_score = ucb()
ts = thompson()

print("Marketing Campaigns\n")
for i in range(4):
    print(campaigns[i], ":", reward[i])

print("\nPerformance")
print("Epsilon-Greedy :", eg)
print("UCB            :", ucb_score)
print("Thompson       :", ts)

scores = [eg, ucb_score, ts]
names = ["Epsilon-Greedy", "UCB", "Thompson Sampling"]

print("\nBest Strategy :", names[np.argmax(scores)])