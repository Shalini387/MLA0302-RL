states = ["Start", "Intersection", "Traffic Signal", "Destination"]

actions = ["Go Straight", "Turn Left", "Turn Right", "Stop"]

policy = ["Go Straight", "Turn Right", "Go Straight", "Stop"]

rewards = [0, 2, 3, 10]

total_reward = 0

print("Autonomous Car Navigation\n")

for i in range(len(states)):
    print("State :", states[i])
    print("Action:", policy[i])
    print("Reward:", rewards[i])
    print()
    total_reward += rewards[i]

print("Total Reward =", total_reward)

print("\nPolicy Evaluation")

if total_reward >= 15:
    print("Policy is Effective")
else:
    print("Policy Needs Improvement")