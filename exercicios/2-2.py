# 2) Faça um programa que converta a temperatura
# de celsius para fahrenheit.

def converte(valor):
    c = (valor * 1.8000) + 32.00
    return c

n1 = float(input("valor celcius: "))
print("valor fahrenheit: ", converte(n1))
