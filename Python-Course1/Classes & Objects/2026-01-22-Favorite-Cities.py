''' 🌆 O exercício (Favorite Cities)

Agora você vai aplicar isso a cidades.

O que o exercício pede:

Criar um arquivo favorite_cities.py

Criar uma classe City

Usar o método __init__() para definir os atributos:

name → string

country → string

population → inteiro (arredondado para o milhar mais próximo)

landmarks → lista de strings

Criar um objeto para:

sua cidade natal

Criar outro objeto para:

uma cidade que você sempre quis visitar'''

class City():
    def __init__(self, name, country, population, landmarks):
        self.name = name
        self.country = country
        self.population = population
        self.landmarks = landmarks

mycity = City('Tiete', 'Brazil', 40000, ['Praca', 'sla', 'sla'])

print(vars(mycity))