# 🎮 Intelligent Game Strategy Learning Using Q-Learning Algorithm

## 📌 Project Description

This project develops an **intelligent self-learning Tic-Tac-Toe game-playing agent** using the **Q-Learning Reinforcement Learning algorithm**.

The agent learns effective game strategies through **trial and error** instead of relying on predefined strategies. It interacts with a **3×3 Tic-Tac-Toe environment**, observes the current board state, selects actions, receives rewards, and updates its **Q-table** after every action.

The agent is trained for **10,000 episodes** using an **ε-greedy policy**, where the exploration rate decreases from **1.0 to 0.01**. After training, the agent is evaluated against a **random player**, and its performance is analyzed using **win rate, rewards, wins, losses, and draws**.

---

## 🎯 Main Objective

The main objective of this project is to develop an intelligent Tic-Tac-Toe agent that can **learn effective game-playing strategies using Q-Learning** and improve its decision-making through repeated gameplay and reward-based learning.

---

## ✨ Key Features

- 🎮 Interactive 3×3 Tic-Tac-Toe game
- 🤖 Q-Learning-based AI agent
- 🧠 Self-learning through trial and error
- 📋 Q-table for storing learned state-action values
- 🎯 ε-greedy action selection
- 📈 10,000 training episodes
- 🔄 Q-table updates after every action
- 📊 Training progress visualization
- 🏆 AI vs Random Player evaluation
- 📈 Win-rate analysis
- 💰 Reward analysis
- 📉 Epsilon decay visualization
- 📋 Q-table/state analysis

---

# 🧩 Project Modules

## Module 1: Game Environment Design

This module creates the **Tic-Tac-Toe game environment** in which the AI agent learns and interacts.

### Components

- **Environment:** 3×3 Tic-Tac-Toe board
- **State:** Current board configuration
- **Actions:** Place the AI mark in an empty cell from **0–8**
- **Win Detection:** Checks rows, columns, and diagonals
- **Draw Detection:** Checks whether all cells are occupied without a winner
- **State Transition:** Updates the board after every valid action
- **Maximum Steps:** 9 moves per episode

### Reward Function

| Game Result | Reward |
|---|---:|
| AI Wins | **+1** |
| Draw | **0** |
| AI Loses | **-1** |

### Technique Used

**Reinforcement Learning – State, Action and Reward Modeling**

### Outcome

A complete Tic-Tac-Toe environment is created for the Q-Learning agent to interact with and learn from.

---

# Module 2: Q-Learning Agent Development

This module implements the **Q-Learning algorithm**, which allows the agent to learn the value of different actions for different board states.

The agent maintains a **Q-table** containing state-action values.

### Q-Learning Formula

```text
Q(s,a) ← Q(s,a) + α[r + γ max Q(s',a') − Q(s,a)]

Where:

- `s` = Current state
- `a` = Selected action
- `r` = Reward received
- `s'` = Next state
- `α` = Learning rate
- `γ` = Discount factor

### Parameters

- **Learning Rate (α): 0.1**
- **Discount Factor (γ): 0.9**

### Key Activities

1. Initialize the Q-table.
2. Observe the current board state.
3. Identify available actions.
4. Select an action.
5. Execute the action.
6. Receive a reward.
7. Observe the next state.
8. Update the Q-value.
9. Store the updated value in the Q-table.

### Technique Used

**Q-Learning Algorithm**

### Outcome

The agent learns which actions are more valuable for different Tic-Tac-Toe board states and gradually improves its game-playing decisions.

---

# Module 3: Training and Strategy Optimization

This module focuses on **training the Q-Learning agent** through repeated gameplay. The agent learns from its previous actions and continuously improves the values stored in the Q-table.

### Training Parameters

| Parameter | Value |
|---|---:|
| Training Episodes | **10,000** |
| Maximum Steps per Episode | **9** |
| Initial Exploration Rate (ε) | **1.0** |
| Minimum Exploration Rate (ε) | **0.01** |
| Learning Rate (α) | **0.1** |
| Discount Factor (γ) | **0.9** |

### ε-Greedy Action Selection

The agent uses an **ε-greedy policy** to balance exploration and exploitation.

### Exploration

The agent selects different actions to discover potentially better strategies.

### Exploitation

The agent selects the action with the highest learned Q-value.

The exploration rate gradually decreases:

```text
ε = 1.0
     ↓
High Exploration
     ↓
Repeated Training
     ↓
ε decreases
     ↓
More Exploitation
     ↓
ε = 0.01
