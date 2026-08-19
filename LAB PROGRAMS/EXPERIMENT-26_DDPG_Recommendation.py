# Question:
# 26) Develop a recommendation system for a streaming service to suggest movies based on user
# feedback, implemented as an MDP and trained using a Deep Deterministic Policy Gradient
# (DDPG) algorithm.

import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Input, Dense

movies = ["Action", "Comedy", "Drama", "Sci-Fi", "Thriller"]
feedback = [8, 6, 7, 10, 5]

actor = Sequential([
    Input(shape=(1,)),
    Dense(16, activation="relu"),
    Dense(1, activation="sigmoid")
])

critic = Sequential([
    Input(shape=(2,)),
    Dense(16, activation="relu"),
    Dense(1)
])

optimizer = tf.keras.optimizers.Adam(0.001)

for episode in range(10):
    for i in range(5):

        state = np.array([[i / 4]], dtype=float)
        reward = feedback[i]

        with tf.GradientTape() as tape:
            action = actor(state)
            value = critic(tf.concat([state, action], axis=1))
            loss = tf.square(reward - value)

        grads = tape.gradient(loss, critic.trainable_variables)
        optimizer.apply_gradients(zip(grads, critic.trainable_variables))

    print("Episode", episode + 1, "Completed")

print("\nMovie Recommendations\n")

scores = []

for i in range(5):
    state = np.array([[i / 4]], dtype=float)
    score = float(actor(state).numpy()[0][0])
    scores.append(score)

    print("Movie :", movies[i])
    print("Preference Score :", round(score, 2))
    print()

best = np.argmax(scores)

print("Best Recommendation :", movies[best])
print("User Feedback :", feedback[best])
print("\nDDPG Training Completed")