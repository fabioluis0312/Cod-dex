"""Crie um programa drive_thru.py com o menu da sua lanchonete favorita.

Defina uma função get_item() que:

recebe um parâmetro → o número do item

retorna o nome do item

Exemplos:

1 → '🍔 Cheeseburger'

2 → '🍟 Fries'

3 → '🥤 Soda'

4 → '🍦 Ice Cream'

5 → '🍪 Cookie'

Depois:

chame a função algumas vezes para testar

crie uma função welcome() que mostra o menu

crie um programa principal que usa input()"""
'''
def welcome():
    print("Bem-vindo ao Ponto da Esfiha!\n Aqui está o nosso menu:\n 1) 🍕 Pizza de Brocolis\n 2) 🍕 Pizza de Portuguesa\n 3) 🥤 Coquinha\n 4) 🥐 Esfiha Doce de Morango c/Chocolate \n 5) 🥐 Esfiha Doce de Banana c/Leite Condensado")

def get_item(item_number):
    menu = {
        1: '🍕 Pizza de Brocolis',
        2: '🍕 Pizza Portuguesa',
        3: '🥤 Coquinha',
        4: '🥐 Esfiha Doce de Morango c/Chocolate',
        5: '🥐 Esfiha Doce de Banana c/Leite Condensado'
    }
    return menu.get(item_number, "Item not found")

welcome()
item_number = int(input("Digite o número do item que você deseja: "))
print(get_item(item_number)) '''

#Minha Versao

def welcome():
    print("Bem-vindo ao Ponto da Esfiha!\n Aqui está o nosso menu:\n 1) 🍕 Pizza de Brocolis\n 2) 🍕 Pizza de Portuguesa\n 3) 🥤 Coquinha\n 4) 🥐 Esfiha Doce de Morango c/Chocolate \n 5) 🥐 Esfiha Doce de Banana c/Leite Condensado\n 6) ❌ Finalizar Pedido")

def get_item(item_number):
    menu = {
        1: '🍕 Pizza de Brocolis',
        2: '🍕 Pizza Portuguesa',
        3: '🥤 Coquinha',
        4: '🥐 Esfiha Doce de Morango c/Chocolate',
        5: '🥐 Esfiha Doce de Banana c/Leite Condensado',
        6: '❌ Finalizar Pedido'
    }
    while item_number != 6:
        item = menu.get(item_number, "Item not found")
        print(item)
        item_number = int(input("Digite o número do item que você deseja (ou 6 para finalizar): "))
    return menu.get(item_number, "Item nao encontrado")

welcome()
item_number = int(input("Digite o número do item que você deseja: "))
print(get_item(item_number))