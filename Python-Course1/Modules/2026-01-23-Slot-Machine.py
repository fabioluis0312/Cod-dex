'''🧩 O que o exercício pede, passo a passo
1️⃣ Criar o arquivo
slot_machine.py

2️⃣ Criar a lista de símbolos

Criar uma lista chamada symbols com:

🍒

🍇

🍉

7️⃣

👉 É só uma lista normal de strings.

3️⃣ Gerar o resultado da rodada

Criar uma variável chamada results

Usar:

o módulo random

o método .choices()

Escolher 3 símbolos aleatórios da lista

⚠️ Importante:

precisa importar o módulo random no topo do arquivo

4️⃣ Mostrar o resultado

Imprimir os 3 símbolos, separados por | (pipe), assim:

🍉 | 🍒 | 🍇


Dica mental:

você tem uma lista

precisa imprimir os elementos separados por um caractere

5️⃣ Verificar se ganhou

Usar um if / else:

Se todos os itens de results forem '7️⃣':

imprimir: Jackpot! 💰

Senão:

imprimir: Thanks for playing!

Aqui está o desafio lógico do exercício.

Pergunta-chave:

“Como verificar se os três itens da lista são iguais a 7️⃣?”'''

import random

symbols = ['🍒', '🍇', '🍉',  '7️⃣']
results =  random.choices(symbols, k=3)

print(' | '.join(results))

if results[0] == '7️⃣' and results[1] == '7️⃣' and results[2] == '7️⃣':
    print("Jackpot! 💰")
else:
    print("Thanks for playing!")

e = input("Voce deseja Continuar?\nY para Sim ou N para Nao\n")

while e == 'Y':
    results =  random.choices(symbols, k=3)

    print(' | '.join(results))

    if results[0] == '7️⃣' and results[1] == '7️⃣' and results[2] == '7️⃣':
        print("Jackpot! 💰")
        break
    else:
        print("Thanks for playing!")
        e = input("Voce deseja Continuar?\nY para Sim ou N para Nao\n")
    

