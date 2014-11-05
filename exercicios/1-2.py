# 2) Crie um programa que receba três números
# float e imprima na tela qual o maior.

n1 = float(input("primeiro n.: "))
n2 = float(input("segundo n.: "))
n3 = float(input("terceiro n.: "))

x = n1
if n2 > x:
    x = n2
if n3 > x:
    x = n3

print(x)

