'''🏦 O exercício (Bank Accounts)

Agora você vai simular uma conta bancária.

O que o exercício pede:

Criar um arquivo chamado bank_accounts.py

Criar uma classe chamada BankAccount

Usar __init__() para definir os atributos:

first_name → string

last_name → string

account_id → inteiro

account_type → string

pin → inteiro

balance → float

Criar três métodos na classe:

.deposit()

adiciona dinheiro ao saldo

retorna o novo saldo

.withdraw()

subtrai dinheiro do saldo

retorna o valor sacado

.display_balance()

imprime o saldo atual

⚠️ Perceba:

alguns métodos retornam

outros imprimem

isso é intencional

Depois disso, você deve:

Criar um objeto da classe BankAccount

Usar esse objeto para:

depositar $96

sacar $25

mostrar o saldo final'''
''' meu Codigo: class BankAccount():
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance
        
    def deposit(self, amount):
            self.balance = self.balance + amount

    def withdraw(self, amount):
            self.balance = self.balance - amount
    def display_balance(self):
            print(f'Seu saldo atual é de: ${self.balance}')

Giovanna = BankAccount('Giovanna', 'Bengozi', 1, 'Sla', 2212, 0.0)

print(vars(Giovanna))

print('--- Operações na conta ---')
num_op = int(input("Ola," + Giovanna.first_name + " o que deseja fazer hoje?\n1) Depositar\n2) Sacar\n3) Ver saldo\nDigite o numero da operacao: "))

while num_op != 0:
    if num_op == 1:
        amount = float(input("Digite o valor que deseja depositar: "))
        Giovanna.deposit(amount)
        print(f'Deposito de ${amount} realizado com sucesso!')
    elif num_op == 2:
        amount = float(input("Digite o valor que deseja sacar: "))
        if amount > Giovanna.balance:
            print("Saldo insuficiente para saque.")
        else:
            Giovanna.withdraw(amount)
            print(f'Saque de ${amount} realizado com sucesso!')
    elif num_op == 3:
        Giovanna.display_balance()
    else:
        print("Opção inválida!")
    
    num_op = int(input("O que deseja fazer agora?\n1) Depositar\n2) Sacar\n3) Ver saldo\n0) Sair\nDigite o numero da operacao: "))

print('--- Fim das operações ---') '''

class BankAccount():
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance
        
    def deposit(self, amount):
            self.balance = self.balance + amount
            return self.balance

    def withdraw(self, amount):
            self.balance = self.balance - amount
            return amount
    def display_balance(self):
            print(f'Seu saldo atual é de: ${self.balance}')

Giovanna = BankAccount('Giovanna', 'Bengozi', 1, 'Sla', 2212, 0.0)

print(vars(Giovanna))

Giovanna.deposit(96)
print("Deposito de $96 realizado com sucesso!")
Giovanna.withdraw(25)
print("Saque de $25 realizado com sucesso!")
Giovanna.display_balance()