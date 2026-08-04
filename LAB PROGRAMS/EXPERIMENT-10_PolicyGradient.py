import pandas as pd

file_path = r"C:\Users\DELL\Downloads\RL_Experiments_1_to_10_Datasets_ZIP\Exp10_Investment.xlsx"

data = pd.read_excel(file_path)

print("Investment Dataset\n")
print(data)

learning_rate = 0.1

investments = data.iloc[:, 0].tolist()
rewards = data.iloc[:, 1].tolist()

policy = [0.5] * len(investments)

print("\nInitial Policy Probabilities")

for i in range(len(investments)):
    print(investments[i], "=", round(policy[i], 2))

for episode in range(10):
    for i in range(len(investments)):
        policy[i] = policy[i] + learning_rate * (rewards[i] / 100)

print("\nOptimized Policy")

for i in range(len(investments)):
    print(investments[i], "=", round(policy[i], 2))

best = policy.index(max(policy))

print("\nBest Investment Strategy :", investments[best])
print("Maximum Reward :", rewards[best])