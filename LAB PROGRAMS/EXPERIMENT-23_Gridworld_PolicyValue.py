import numpy as np
import matplotlib.pyplot as plt

grid = 4
goal = (3, 3)
gamma = 0.9

policies = {
    "Right": "R",
    "Down": "D"
}

def evaluate(action):
    value = np.zeros((grid, grid))

    for _ in range(100):
        new_value = value.copy()

        for r in range(grid):
            for c in range(grid):

                if (r, c) == goal:
                    continue

                if action == "R":
                    nr, nc = r, min(c + 1, grid - 1)
                else:
                    nr, nc = min(r + 1, grid - 1), c

                reward = 10 if (nr, nc) == goal else -1
                new_value[r, c] = reward + gamma * value[nr, nc]

        value = new_value

    return value

for name, action in policies.items():

    value = evaluate(action)

    print("\nPolicy :", name)
    print(np.round(value, 2))

    plt.imshow(value)
    plt.colorbar()
    plt.title("Value Function - " + name + " Policy")
    plt.xlabel("Column")
    plt.ylabel("Row")
    plt.show()
    