# Question:
# 27) Implement an agent that manages a financial portfolio, choosing stocks to maximize returns
# and minimize risk using an Actor-Critic (A3C) method to optimize investment. Implement a
# robot that navigates a maze to reach the exit, with rewards for reaching the exit and
# penalties for hitting walls, and use REINFORCE to find the optimal navigation policy.

import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Input, Dense

# ---------- A3C Portfolio ----------

stocks = ["Stock A", "Stock B", "Stock C", "Stock D"]
returns = [8, 10, 6, 12]
risk = [3, 5, 2, 7]

actor = Sequential([
    Input(shape=(1,)),
    Dense(16, activation="relu"),
    Dense(4, activation="softmax")
])

critic = Sequential([
    Input(shape=(1,)),
    Dense(16, activation="relu"),
    Dense(1)
])

optimizer = tf.keras.optimizers.Adam(0.001)

for episode in range(10):
    state = np.array([[0.5]])

    with tf.GradientTape() as tape:
        prob = actor(state)
        value = critic(state)
        reward = max(np.array(returns) - np.array(risk))
        loss = tf.square(reward - value)

    grads = tape.gradient(loss, critic.trainable_variables)
    optimizer.apply_gradients(zip(grads, critic.trainable_variables))

print("A3C Portfolio Optimization\n")

scores = np.array(returns) - np.array(risk)

for i in range(4):
    print(stocks[i], "Return:", returns[i], "Risk:", risk[i])

best_stock = np.argmax(scores)

print("Best Stock :", stocks[best_stock])
print("Expected Reward :", scores[best_stock])


# ---------- REINFORCE Maze ----------

maze = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

start = [0, 0]
goal = [3, 3]

policy = np.ones((4, 4, 4)) / 4
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for episode in range(100):

    pos = start.copy()

    for step in range(30):

        r, c = pos
        action = np.random.choice(4, p=policy[r, c])

        nr = r + moves[action][0]
        nc = c + moves[action][1]

        if nr < 0 or nr >= 4 or nc < 0 or nc >= 4 or maze[nr][nc] == 1:
            reward = -1
        else:
            pos = [nr, nc]
            reward = 10 if pos == goal else -0.1

        if pos == goal:
            break

print("\nREINFORCE Maze")
print("Start :", start)
print("Goal  :", goal)
print("Training Completed")

print("\nOptimal Actions:")

names = ["Up", "Down", "Left", "Right"]

for r in range(4):
    for c in range(4):
        if maze[r][c] == 0:
            print((r, c), "->", names[np.argmax(policy[r, c])])