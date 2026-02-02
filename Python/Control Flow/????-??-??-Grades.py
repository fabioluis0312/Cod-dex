import random

grade = random.randint(0, 100)
print(grade)
if grade >= 55:
    print("Voce Passou")
else:
    print("Reprovou")