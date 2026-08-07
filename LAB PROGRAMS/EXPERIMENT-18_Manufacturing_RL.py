import pandas as pd

file_path = r"C:\Users\DELL\Downloads\RL_Experiments_11_to_20_Datasets\Exp18_Manufacturing.csv"

data = pd.read_csv(file_path)

print("Manufacturing Dataset\n")
print(data)

settings = data["Machine_Setting"]
quality = data["Quality"]
rewards = data["Reward"]

values = [0] * len(settings)

lr = 0.1
gamma = 0.9

for _ in range(10):
    for i in range(len(values)):
        values[i] += lr * (rewards[i] + gamma * values[i] - values[i])

print("\nValue Function\n")

for i in range(len(values)):
    print("Machine Setting :", settings[i])
    print("Quality         :", quality[i])
    print("Reward          :", rewards[i])
    print("Value           :", round(values[i],2))
    print()

best = values.index(max(values))

print("Optimal Machine Setting :", settings[best])
print("Maximum Reward :", rewards[best])