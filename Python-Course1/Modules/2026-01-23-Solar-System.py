''' 🧩 O que o exercício pede, passo a passo
1️⃣ Criar o arquivo
solar_system.py

2️⃣ Importações (parte mais importante do exercício)

No topo do arquivo:

Importar π (pi) do módulo math

Importar choice do módulo random, mas:

renomear choice para ch

Pergunta-chave:

“Por que usar from aqui?”

Resposta:

para usar pi direto

para chamar ch() em vez de random.choice()

3️⃣ Lista de planetas

Copiar exatamente a lista:

['Mercury', 'Venus', 'Earth', 'Mars', 'Saturn']

4️⃣ Escolher um planeta aleatório

Usar ch() (que é o choice renomeado)

Escolher um planeta aleatório

Guardar em random_planet

5️⃣ Fórmula da área da esfera

A fórmula da área da superfície de uma esfera é:

area = 4 × π × r²


Você já tem:

π → veio do math

falta definir r (raio)

6️⃣ Definir o raio (r) com if / elif / else

Você deve:

comparar random_planet

atribuir o valor correto de r

Tabela mental:

Planeta	Raio (km)
Mercury	2440
Venus	6052
Earth	6371
Mars	3390
Saturn	58232

Se não cair em nenhum, imprimir:

Oops! An error occurred.

7️⃣ Calcular e imprimir o resultado

Depois de ter:

random_planet

r

pi

Você:

calcula a área

imprime:

nome do planeta

área calculada'''

from math import pi
from random import choice as ch



planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Saturn']

random_planet = ch(planets)

if random_planet == 'Mercury':
    r = 2440
elif random_planet == 'Venus':
    r = 6052
elif random_planet == 'Earth':
    r = 6371
elif random_planet == 'Mars':
    r = 3390
elif random_planet == 'Saturn':
    r = 58232
else:
    print("Oops! An error occurred.")

area = 4 * pi * r**2

print(random_planet, area)