import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

import warnings
warnings.filterwarnings("ignore")

import gymnasium as gym
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.optimizers import Adam

env = gym.make("MountainCar-v0")

model = Sequential([
    Input(shape=(2,)),
    Dense(24, activation="relu"),
    Dense(24, activation="relu"),
    Dense(env.action_space.n, activation="linear")
])

model.compile(optimizer=Adam(), loss="mse")

episodes = 2

for episode in range(episodes):

    state, info = env.reset()
    state = np.reshape(state, (1, 2))

    total_reward = 0

    for step in range(100):

        q_values = model.predict(state, verbose=0)
        action = np.argmax(q_values[0])

        next_state, reward, terminated, truncated, info = env.step(action)

        total_reward += reward

        state = np.reshape(next_state, (1, 2))

        if terminated or truncated:
            break

    print(f"Episode {episode + 1}")
    print("Steps Taken :", step + 1)
    print("Total Reward:", total_reward)
    print()

env.close()

print("Training Completed Successfully")