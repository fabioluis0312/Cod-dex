bill = [13.99, 28.75, 9.99, 9.99, 6.95, 7.45, 16.45, 16.45]

total = 0

# somar todos os valores da lista
for price in bill:
    total = total + price

# dividir o total por 4 pessoas
my_share = total / 4

# imprimir o valor que cada pessoa paga
print(my_share)
