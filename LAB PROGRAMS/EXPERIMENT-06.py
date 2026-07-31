import random

ads = ["Ad A", "Ad B", "Ad C"]

ctr = [5, 10, 8]

print("Advertisements:", ads)
print("Click Rates:", ctr)

# Epsilon-Greedy
epsilon = 0.2
click1 = 0

for i in range(10):
    if random.random() < epsilon:
        ad = random.randint(0, 2)
    else:
        ad = ctr.index(max(ctr))
    click1 += ctr[ad]

print("\nEpsilon-Greedy Clicks =", click1)

# UCB
click2 = 0

for i in range(10):
    ad = ctr.index(max(ctr))
    click2 += ctr[ad]

print("UCB Clicks =", click2)

# Thompson Sampling
click3 = 0

for i in range(10):
    ad = random.randint(0, 2)
    click3 += ctr[ad]

print("Thompson Sampling Clicks =", click3)

print("\nBest Algorithm")

if click1 >= click2 and click1 >= click3:
    print("Epsilon-Greedy")
elif click2 >= click1 and click2 >= click3:
    print("UCB")
else:
    print("Thompson Sampling")