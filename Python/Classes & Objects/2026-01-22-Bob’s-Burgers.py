'''🍔 O exercício em si (Bob’s Burgers)

No exercício anterior, você criou a classe Restaurant.

Agora você deve:

Criar um novo arquivo chamado bobs_burgers.py

Criar um objeto da classe Restaurant chamado bobs_burgers

Atribuir a esse objeto os seguintes valores:

nome: 'Bob's Burgers'

categoria: 'American Diner'

avaliação: 4.7

delivery: False

Criar mais dois objetos da classe Restaurant

usando restaurantes que você gosta

Usar print(vars()) para mostrar os dados dos três restaurantes '''

#Vou Reutilizar o codigo anterior

class Restaurant():
    name = ''
    category = ''
    rating = 0.0
    delivery = bool
    
bobs_burgers = Restaurant()

bobs_burgers.name = 'Bob\'s Burgers'
bobs_burgers.category = 'American Diner'
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False

print(vars(bobs_burgers))