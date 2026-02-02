import random

print("===================\nRock Paper Scissors Lizard Spock\n===================\n1) ✊\n2) ✋\n3) ✌️\n4) 🦎\n5) 🖖")

player = int(input("Pick a number: "))

if player == 1:
    print("You chose: ✊")
elif player == 2:
    print("You chose: ✋")
elif player == 3:
    print("You chose: ✌️")
elif player == 4:
    print("You chose: 🦎")
elif player == 5:
    print("You chose: 🖖")
else:
    print("Invalid input")
    exit()

cpu = random.randint(1, 5)
if cpu == 1:
    print("CPU chose: ✊")
elif cpu == 2:
    print("CPU chose: ✋")
elif cpu == 3:
    print("CPU chose: ✌️")
elif cpu == 4:
    print("CPU chose: 🦎")
elif cpu == 5:
    print("CPU chose: 🖖")

winning_combos = {
    1: [3, 4],
    2: [1, 5],
    3: [2, 4],
    4: [2, 5],
    5: [1, 3],
}

if player == cpu:
    print("It's a tie!")
elif cpu in winning_combos[player]:
    print("You win! 🎉")
else:
    print("CPU wins! 😢")