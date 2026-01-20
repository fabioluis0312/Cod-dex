# the_cyclone.py

# Pergunta a altura e créditos do usuário
height = int(input("Qual é a sua altura em cm? "))
credits = int(input("Quantos créditos você tem? "))

# Regras do passeio
if height >= 137 and credits >= 10:
    print("Aproveite o passeio!")
elif height < 137 and credits >= 10:
    print("Você não é alto o suficiente para andar")
elif height >= 137 and credits < 10:
    print("Você não tem créditos suficientes")
else:
    print("Você não atende a nenhum dos requisitos para o passeio")
