"""🧠 Agora o exercício de verdade (fintech)

Você vai analisar preços de uma ação (AMC) em janeiro de 2023.

Lista de preços (DADO FIXO)
stock_prices = [
  34.68, 36.09, 34.94, 33.97, 34.68,
  35.82, 43.41, 44.29, 44.65, 53.56,
  49.85, 48.71, 48.71, 49.94, 48.53,
  47.03, 46.59, 48.62, 44.21, 47.21
]

🎯 O que você precisa implementar (sem inventar moda)

Criar 3 funções, usando essa lista global:

price_at(x)
→ retorna o preço do dia x

max_price(a, b)
→ retorna o maior preço entre os dias a e b

min_price(a, b)
→ retorna o menor preço entre os dias a e b

⚠️ Importante:

Dias vão de 1 a 20

Lista em Python começa no índice 0

Então: dia 1 = índice 0

Se você errar isso, tudo quebra."""

stock_prices = [
    34.68, 36.09, 34.94, 33.97, 34.68,
    35.82, 43.41, 44.29, 44.65, 53.56,
    49.85, 48.71, 48.71, 49.94, 48.53,
    47.03, 46.59, 48.62, 44.21, 47.21
]


#1
def price_at(day):
    return stock_prices[day - 1]

print("Preco do dia 1: ",price_at(1))
print("Preco do dia 10: ",price_at(10))
print("Preco do dia 20: ",price_at(20))

#2
def max_price(day_a, day_b):
    return max(stock_prices[day_a - 1 : day_b])


print("Preco Maximo entre o dia 1 e o dia 10:", max_price(1, 10));

#3
def min_price(day_a, day_b):
    return min(stock_prices[day_a - 1 : day_b])


print("Preco Minimo entre o dia 1 e o dia 10:", min_price(1, 10));