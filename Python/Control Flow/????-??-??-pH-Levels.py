ph = float(input("Digite seu pH: "))

if ph > 7:
    print("Basic")
elif ph < 7:
    print("Acidic")
else:
    print("Neutral")
