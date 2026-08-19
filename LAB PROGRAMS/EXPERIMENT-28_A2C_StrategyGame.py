# Question:
# 28) Develop an AI agent to play a real-time strategy game (e.g., Age of Empires) using Actor-
# Critic methods. Implement the actor and critic networks in Python and train the agent to build
# structures, gather resources, and engage in strategic combat.

import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Input, Dense

actions = ["Gather", "Build", "Attack"]
rewards = [5, 3, 10]

actor = Sequential([
    Input(shape=(1,)),
    Dense(16, activation="relu"),
    Dense(3, activation="softmax")
])

critic = Sequential([
    Input(shape=(1,)),
    Dense(16, activation="relu"),
    Dense(1)
])

actor_opt = tf.keras.optimizers.Adam(0.001)
critic_opt = tf.keras.optimizers.Adam(0.001)

for episode in range(10):

    state = np.array([[0.5]])

    with tf.GradientTape() as at, tf.GradientTape() as ct:

        prob = actor(state)
        value = critic(state)

        action = np.random.choice(3, p=prob.numpy()[0])
        reward = rewards[action]

        advantage = reward - value[0][0]

        actor_loss = -tf.math.log(prob[0][action]) * tf.stop_gradient(advantage)
        critic_loss = tf.square(advantage)

    ag = at.gradient(actor_loss, actor.trainable_variables)
    cg = ct.gradient(critic_loss, critic.trainable_variables)

    actor_opt.apply_gradients(zip(ag, actor.trainable_variables))
    critic_opt.apply_gradients(zip(cg, critic.trainable_variables))

    print("Episode", episode + 1, "Reward =", reward)

print("\nLearned Strategy\n")

prob = actor(np.array([[0.5]])).numpy()[0]
best = np.argmax(prob)

for i in range(3):
    print(actions[i], "Probability :", round(float(prob[i]), 2))

print("\nBest Action :", actions[best])
print("Reward :", rewards[best])

print("\nActor-Critic Training Completed")