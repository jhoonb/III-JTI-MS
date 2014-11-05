# 5) Receba o valor do produto e o percentual
# de desconto dele, calcule qual o valor do
# produto com o desconto e mostre na tela.


def desconto(v, p):
    valor = v - (v * (p / 100))
    return valor

valor = float(input("valor do produto: "))
per = float(input("% de desconto: "))
print("valor com desconto: ", desconto(valor, per))
