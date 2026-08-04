import pandas as pd

file_path = r"C:\Users\DELL\Downloads\RL_Experiments_1_to_10_Datasets_ZIP\Exp1_RobotGrid.xlsx"

grid = pd.read_excel(file_path, header=None)

print("Grid Environment\n")
print(grid)

rows = len(grid)
cols = len(grid.columns)

row = 0
col = 0

reward = 0

policy = [
    "Right", "Right", "Down", "Right", "Down",
    "Left", "Down", "Down", "Right", "Right"
]

print("\nRobot Navigation\n")

for move in policy:

    if move == "Right" and col < cols - 1:
        col += 1

    elif move == "Left" and col > 0:
        col -= 1

    elif move == "Up" and row > 0:
        row -= 1

    elif move == "Down" and row < rows - 1:
        row += 1

    cell = grid.iloc[row, col]

    if cell == "D":
        reward += 1
        print(move, "-> Dirt Found (+1)")

    elif cell == "X":
        reward -= 1
        print(move, "-> Obstacle Hit (-1)")

    elif cell == "G":
        print(move, "-> Goal Reached")

    else:
        print(move, "-> Empty Cell")

    print("Current Position:", (row, col))
    print("Total Reward:", reward)
    print()

print("Final Reward =", reward)