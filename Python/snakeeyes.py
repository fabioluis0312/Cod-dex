import random

total = 0

while total != 2:
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2

    if total != 2:
        print("Nope")

print("Snake Eyes!")
print("Die 1: ", die1, "Die 2:", die2, "Total:", total)
