# 3) Modifique o programa a cima para imprimir o menor.

n1 = float(input("primeiro n.: "))
n2 = float(input("segundo n.: "))
n3 = float(input("terceiro n.: "))

x = n1
if x > n2:
    x = n2
if x > n3:
    x = n3

print(x)
