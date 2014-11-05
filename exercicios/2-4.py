# 4) Faça um programa que some todos os números
# desta lista: numeros = [1,2,34,9,78,555,444444,333233,2231,122]

def somalista(n):
    soma = 0
    for i in n:
        soma += i
    return soma


numeros = [1,2,34,9,78,555,444444,333233,2231,122]
soma = somalista(numeros)
print("soma: ", soma)
