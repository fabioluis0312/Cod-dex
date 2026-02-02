'''🧩 O exercício (Pokédex)

Desde 1996, Pokémon diverte jogadores do mundo todo.
A Pokédex é um dispositivo que guarda informações dos Pokémon vistos ou capturados.

1️⃣ Criar o arquivo

Crie um arquivo chamado:

pokedex.py

2️⃣ Criar a classe Pokemon

Defina uma classe Pokemon com os seguintes atributos, usando __init__():

entry → número da Pokédex (inteiro)

name → nome do Pokémon (string)

types → tipos do Pokémon (lista de strings)

description → descrição (string)

is_caught → se foi capturado ou não (boolean)

⚠️ Todos esses atributos devem ser recebidos no __init__.

3️⃣ Criar o método .speak()

Método de instância (usa self)

Deve imprimir o som do Pokémon

Normalmente, Pokémon “falam” o próprio nome

Então o método deve imprimir o nome duas vezes

Exemplo mental:

Pikachu Pikachu

4️⃣ Criar o método .display_details()

Esse método deve imprimir todas as informações do Pokémon no formato abaixo:

Entry Number: 25
Name: Pikachu
Type: Electric
Description: It has small electric sacs on both its cheeks...
Pikachu has already been caught!


Observações importantes:

Use os valores guardados no objeto (self)

O texto final muda dependendo de is_caught

se True → “has already been caught!”

se False → algo como “has not been caught yet!”

5️⃣ Criar objetos

Criar três objetos da classe Pokemon

Para cada um:

chamar .speak() ou

chamar .display_details()

Não precisa usar os dois em todos, mas precisa usar métodos. '''

class Pokemon():
    def __init__(self, entry, name, types, description, is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught
    
    def speak(self):
        print(self.name + ',', self.name)
    
    def display_details(self):
        print(f"Entry Number: {self.entry}\nName: {self.name}\nType: {', '.join(self.types)}\nDescription: {self.description}")
        if self.is_caught:
            print(f"{self.name} has already been caught!")
        else:
            print(f"{self.name} has not been caught yet!")

Pikachu = Pokemon(25, 'Pikachu', ['Electric'], 'It has small electric sacs on both its cheeks...', True)

Pikachu.speak()
Pikachu.display_details()