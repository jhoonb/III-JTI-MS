# 6) Faça um programa que simule uma calculadora simples,
# informe qual operação: +, /, %, -, *
# logo após informe dois valores, retorne o valor dessa operação.

def soma(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    if b != 0:
        return a/b
    else:
        return "divisao por zero"

def rest(a, b):
    if b != 0:
        return a%b
    else:
        return "divisao por zero"

#----------------------------------------------
def calculadora(op, a, b):

    if op == "*":
        return mul(a, b)
    
    elif op == "/":
        return div(a, b)

    elif op == "%":
        return rest(a, b)
    
    elif op == "-":
        return sub(a, b)

    elif op == "+":
        return soma(a, b)
    else:
        return "comando inválido"

#-------------------------------------------------

op = input("informa a operação (+, /, %, -, *): ")
v1 = float(input("informe o valor 1: "))
v2 = float(input("informe o valor 2: "))
print("resultado: ", calculadora(op, v1, v2))
