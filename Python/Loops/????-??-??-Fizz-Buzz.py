def fizzbuzz_label(n):# n e um numero
    if is_multiple(n, 3) and is_multiple(n, 5):# se n e multiplo de 3 e 5
        return "FizzBuzz"
    elif is_multiple(n, 3): # se n eh multiplo de 3
        return "Fizz"
    elif is_multiple(n, 5): # se n eh multiplo de 5
        return "Buzz"
    else:
        return str(n) # se n nao eh multiplo de 3 ou 5 ele retorna n(string, numero inteiro)


def is_multiple(n, m): #defina is_multiple que recebe dois valores n e m, n e mutiplo de m que retorna verdadeiro ou falso, sendo n um numero inteiro
    return n % m == 0


for i in range(1, 101):  # para i de 1 a 100
    print(fizzbuzz_label(i))
