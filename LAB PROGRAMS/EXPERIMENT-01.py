import gymnasium as gym

env = gym.make("FrozenLake-v1", is_slippery=False)

state, info = env.reset()

print("Initial State:", state)

for i in range(10):

    action = env.action_space.sample()

    next_state, reward, terminated, truncated, info = env.step(action)

    print("Step:", i + 1)
    print("Action:", action)
    print("Next State:", next_state)
    print("Reward:", reward)
    print()

    if terminated or truncated:
        print("Episode Finished")
        break

env.close()