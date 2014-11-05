# 3) Faça um programa que converta a temperatura
# de fahrenheit para celsius.


def converte(valor):
    c = (valor - 32) / 1.8
    return c
    
n1 = float(input("valor fahrenheit: "))
print("valor celcius: ", converte(n1))
