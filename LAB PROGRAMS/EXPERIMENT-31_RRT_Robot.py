# Question:
# 31) An autonomous exploration robot needs to navigate and map an unknown environment.
# Implement a sampling-based planning algorithm (e.g., RRT, RRT*, or PRM) to plan collision-
# free paths for the robot to explore efficiently.

import numpy as np
import matplotlib.pyplot as plt

start = np.array([5, 5])
goal = np.array([95, 95])

obstacles = [[20, 20, 25, 10], [55, 15, 20, 25],
             [30, 55, 30, 15], [70, 60, 15, 25]]

nodes = [start]
parents = [-1]

def collision(p):
    return any(x <= p[0] <= x+w and y <= p[1] <= y+h
               for x, y, w, h in obstacles)

for _ in range(3000):
    p = np.random.randint(0, 101, 2)

    d = [np.linalg.norm(n-p) for n in nodes]
    i = np.argmin(d)

    direction = p - nodes[i]
    dist = np.linalg.norm(direction)

    if dist == 0:
        continue

    new = nodes[i] + direction / dist * min(3, dist)

    if not collision(new):
        nodes.append(new)
        parents.append(i)

        if np.linalg.norm(new-goal) < 3:
            nodes.append(goal)
            parents.append(len(nodes)-2)
            break

path = []
i = len(nodes)-1

while i != -1:
    path.append(nodes[i])
    i = parents[i]

path = np.array(path[::-1])

for x, y, w, h in obstacles:
    plt.gca().add_patch(plt.Rectangle((x, y), w, h))

plt.plot(path[:,0], path[:,1], "b-", linewidth=2)
plt.plot(*start, "go")
plt.plot(*goal, "ro")

plt.xlim(0, 100)
plt.ylim(0, 100)
plt.title("Robot RRT Path Planning")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show()

print("RRT Robot Exploration Completed")
print("Path Points :", len(path))