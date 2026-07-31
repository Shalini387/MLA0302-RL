import matplotlib.pyplot as plt

states = ["Warehouse", "Point A", "Point B", "Point C", "Destination"]

rewards = [0, 2, 4, 6, 10]

gamma = 0.9

values = [0, 0, 0, 0, 0]

for i in range(10):
    values[4] = rewards[4]
    values[3] = rewards[3] + gamma * values[4]
    values[2] = rewards[2] + gamma * values[3]
    values[1] = rewards[1] + gamma * values[2]
    values[0] = rewards[0] + gamma * values[1]

print("State Value Function")

for i in range(len(states)):
    print(states[i], "=", round(values[i], 2))

plt.bar(states, values)
plt.title("State Value Function")
plt.xlabel("States")
plt.ylabel("Value")
plt.show()