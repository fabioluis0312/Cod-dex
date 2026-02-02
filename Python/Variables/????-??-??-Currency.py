
pesos = float(input("Quanto tem em Pesos: "))
soles = float(input("Quanto tem em Soles: "))
reais = float(input("Quanto tem em Reais: "))


usd_pesos = 1471
usd_soles = 3.47
usd_reais = 5.37

total = (pesos / usd_pesos) + (soles / usd_soles) + (reais / usd_reais)
valorusd = f'O valor total em USD é: {total:.2f}'
print(valorusd)