guess = 0
tries = 0

while guess != 6:
    guess = int(input("Guess the number:  "))
    tries += 1

if guess == 6:
    print("You got it!")
else:
    print("Out of tries! The correct number was 6.")
