import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Dense

file_path = r"C:\Users\DELL\Downloads\Exp29_A2C_AutoRacing.csv"

data = pd.read_csv(file_path)

print("Autonomous Racing Dataset\n")
print(data)

states = data[["Speed", "Position", "Direction", "Track_Condition"]].values
rewards = data["Reward"].values

actions = ["Brake", "Maintain", "Accelerate"]

actor = Sequential([
    Input(shape=(4,)),
    Dense(24, activation="relu"),
    Dense(24, activation="relu"),
    Dense(3, activation="softmax")
])

critic = Sequential([
    Input(shape=(4,)),
    Dense(24, activation="relu"),
    Dense(24, activation="relu"),
    Dense(1)
])

actor_optimizer = tf.keras.optimizers.Adam(0.001)
critic_optimizer = tf.keras.optimizers.Adam(0.001)

for episode in range(10):

    total_reward = 0

    for i in range(len(states)):

        state = states[i].reshape(1, 4)
        reward = rewards[i]

        with tf.GradientTape() as tape1, tf.GradientTape() as tape2:

            probability = actor(state)
            value = critic(state)

            action = np.random.choice(3, p=probability.numpy()[0])

            advantage = reward - value[0][0]

            actor_loss = -tf.math.log(probability[0][action]) * tf.stop_gradient(advantage)
            critic_loss = tf.square(advantage)

        actor_grads = tape1.gradient(actor_loss, actor.trainable_variables)
        critic_grads = tape2.gradient(critic_loss, critic.trainable_variables)

        actor_optimizer.apply_gradients(zip(actor_grads, actor.trainable_variables))
        critic_optimizer.apply_gradients(zip(critic_grads, critic.trainable_variables))

        total_reward += reward

    print("Episode", episode + 1, "Total Reward =", total_reward)

print("\nLearned Racing Policy\n")

for i in range(len(states)):
    probability = actor(states[i].reshape(1, 4)).numpy()[0]
    best = np.argmax(probability)

    print("Speed :", states[i][0])
    print("Lap Time :", data["Lap_Time"][i])
    print("Best Action :", actions[best])
    print("Reward :", rewards[i])
    print()

print("A2C Training Completed")