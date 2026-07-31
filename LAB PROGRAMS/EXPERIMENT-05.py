states = ["Taxi Stand", "Pick-up Point", "Passenger", "Destination"]

actions = ["Up", "Down", "Left", "Right"]

rewards = [0, 2, 5, 10]

gamma = 0.9

values = [0, 0, 0, 0]

for i in range(10):
    values[3] = rewards[3]
    values[2] = rewards[2] + gamma * values[3]
    values[1] = rewards[1] + gamma * values[2]
    values[0] = rewards[0] + gamma * values[1]

print("States:", states)
print("Actions:", actions)

print("\nOptimal State Values")

for i in range(len(states)):
    print(states[i], "=", round(values[i], 2))

print("\nOptimal Dispatch Policy")

print("Taxi Stand -> Pick-up Point")
print("Pick-up Point -> Passenger")
print("Passenger -> Destination")
print("Destination -> Stop")