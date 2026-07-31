states = ["Warehouse", "Point A", "Point B", "Destination"]

actions = ["Right", "Down"]

policy = ["Right", "Down", "Right", "Goal"]

rewards = [0, 2, 3, 5]

gamma = 0.9

values = [0, 0, 0, 0]

for i in range(10):
    values[3] = rewards[3]
    values[2] = rewards[2] + gamma * values[3]
    values[1] = rewards[1] + gamma * values[2]
    values[0] = rewards[0] + gamma * values[1]

print("States:", states)
print("Actions:", actions)

print("\nOptimal Policy")

for i in range(len(policy)):
    print(states[i], "->", policy[i])

print("\nState Values")

for i in range(len(values)):
    print(states[i], "=", round(values[i], 2))