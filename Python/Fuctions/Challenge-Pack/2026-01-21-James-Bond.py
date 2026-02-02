"""James Bond

James Bond é um personagem clássico do cinema que luta contra vilões e se apresenta de forma icônica:
“Bond, James Bond.”

Crie uma função chamada greetings() que recebe dois parâmetros:

first_name
last_name

A função deve imprimir a frase com:
o sobrenome
uma vírgula
o nome completo
Depois, chame a função usando o seu próprio nome, como no exemplo:

# greetings('Richard', 'Hendricks')


A saída deve ser:

Hendricks, Richard Hendricks


Nota: essa função não tem return."""


def greetings(first_name, last_name):
    print(f"{last_name}, {first_name} {last_name}")

greetings('James', 'Bond')
