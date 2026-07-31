import gymnasium as gym

env = gym.make("FrozenLake-v1", is_slippery=False)

states = ["Start", "Pick Item", "Obstacle", "Goal"]
actions = ["Up", "Down", "Left", "Right"]
rewards = [0, 2, -2, 5]

gamma = 0.9

values = [0, 0, 0, 0]

for i in range(10):
    values[3] = rewards[3]
    values[2] = rewards[2]
    values[1] = rewards[1] + gamma * values[3]
    values[0] = rewards[0] + gamma * values[1]

print("States:", states)
print("Actions:", actions)

print("\nValue Function")

for i in range(len(states)):
    print(states[i], "=", round(values[i], 2))

env.close()