''' Você deve criar uma função:

dog_years(name, age)


Onde:

name → string (nome do cachorro)

age → inteiro (idade do cachorro)

Regra:

1 ano de cachorro = 7 anos humanos

Calcular: age * 7

Retornar uma string (não imprimir)

Formato EXATO da string (isso é crítico):

<nome> is <idade_humana> years old in human years.


Pontuação, espaços e ponto final importam. '''

def dog_years(name, age):
    age = age * 7
    return f"{name} is {age} years old in human years."

print(dog_years("Petunia", 3))