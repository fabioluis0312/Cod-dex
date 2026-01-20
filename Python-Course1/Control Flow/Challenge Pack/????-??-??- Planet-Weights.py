earth_weight = float(input("Enter your weight on Earth (in pounds): "))
planet_number = int(input("Enter the planet number (1-7): "))

if planet_number == 1:
    relative_gravity = 0.38
elif planet_number == 2:
    relative_gravity = 0.91
elif planet_number == 3:
    relative_gravity = 0.38
elif planet_number == 4:
    relative_gravity = 2.53
elif planet_number == 5:
    relative_gravity = 1.07
elif planet_number == 6:
    relative_gravity = 0.89
elif planet_number == 7:
    relative_gravity = 1.14
else:
    print("Invalid planet number")
    relative_gravity = None

if relative_gravity is not None:
    destination_weight = earth_weight * relative_gravity
    print(f"Your weight on the planet is {destination_weight:.2f} pounds.")