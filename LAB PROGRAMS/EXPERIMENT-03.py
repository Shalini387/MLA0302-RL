import random

prices = [100, 200, 300]
revenues = [10, 20, 15]

print("Prices:", prices)
print("Revenues:", revenues)

# Epsilon-Greedy
epsilon = 0.2
total1 = 0

for i in range(10):
    if random.random() < epsilon:
        arm = random.randint(0, 2)
    else:
        arm = revenues.index(max(revenues))
    total1 += revenues[arm]

print("\nEpsilon-Greedy Revenue =", total1)

# UCB
total2 = 0

for i in range(10):
    arm = revenues.index(max(revenues))
    total2 += revenues[arm]

print("UCB Revenue =", total2)

# Thompson Sampling
total3 = 0

for i in range(10):
    arm = random.randint(0, 2)
    total3 += revenues[arm]

print("Thompson Sampling Revenue =", total3)

print("\nBest Strategy")

if total1 >= total2 and total1 >= total3:
    print("Epsilon-Greedy")
elif total2 >= total1 and total2 >= total3:
    print("UCB")
else:
    print("Thompson Sampling")