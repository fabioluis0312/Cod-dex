# Chapéu Seletor

# Inicializando pontuações das casas
grifinoria = 0
corvinal = 0
lufalufa = 0
sonserina = 0

# Q1
q1 = int(input("Do you like Dawn or Dusk?\n1) Dawn\n2) Dusk\nEscolha 1 ou 2: "))
if q1 == 1:
    grifinoria += 1
    corvinal += 1
elif q1 == 2:
    lufalufa += 1
    sonserina += 1
else:
    print("Entrada errada")

# Q2
q2 = int(input("When I’m dead, I want people to remember me as:\n1) The Good\n2) The Great\n3) The Wise\n4) The Bold\nEscolha de 1 a 4: "))
if q2 == 1:
    lufalufa += 2
elif q2 == 2:
    sonserina += 2
elif q2 == 3:
    corvinal += 2
elif q2 == 4:
    grifinoria += 2
else:
    print("Entrada errada")

# Q3
q3 = int(input("Which kind of instrument most pleases your ear?\n1) The violin\n2) The trumpet\n3) The piano\n4) The drum\nEscolha de 1 a 4: "))
if q3 == 1:
    sonserina += 4
elif q3 == 2:
    lufalufa += 4
elif q3 == 3:
    corvinal += 4
elif q3 == 4:
    grifinoria += 4
else:
    print("Entrada errada")

# Imprimindo pontuações
print(f"\nPontuações:")
print(f"Grifinória: {grifinoria}")
print(f"Corvinal: {corvinal}")
print(f"Lufa-Lufa: {lufalufa}")
print(f"Sonserina: {sonserina}")

# Descobrindo a casa com mais pontos
casas = {
    "Grifinória": grifinoria,
    "Corvinal": corvinal,
    "Lufa-Lufa": lufalufa,
    "Sonserina": sonserina
}

max_pontos = max(casas.values())
melhor_casas = [casa for casa, pontos in casas.items() if pontos == max_pontos]

print("\nSua casa é:", ", ".join(melhor_casas))
