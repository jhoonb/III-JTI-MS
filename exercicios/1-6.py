#6) Usando o mesmo programa a cima, só que quando finalizar
# imprima a média aritmética dos números lidos

soma = 0
cont = 1

while True:

    num = int(input("insira: "))
    if num == -1:
        print("valor: ", soma , " | média: ", soma/cont)
        break
    
    soma += num
    cont += 1
