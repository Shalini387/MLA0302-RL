import random

states = ["Representative A", "Representative B", "Representative C"]

rewards = [5, 8, 10]

episodes = 10

values = [0, 0, 0]

counts = [0, 0, 0]

for i in range(episodes):

    state = random.randint(0, 2)

    values[state] += rewards[state]

    counts[state] += 1

print("Estimated State Values\n")

for i in range(len(states)):
    if counts[i] != 0:
        values[i] = values[i] / counts[i]
    print(states[i], "=", round(values[i], 2))

best = values.index(max(values))

print("\nBest Assignment Policy:", states[best])