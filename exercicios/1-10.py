# 10) Entre os números 1 e 10000 quantos são impares
# excluindo os múltiplos de 7 e 3?

cont = 0
for i in range(1, 10001, 2):
    if i % 3 != 0 and i % 7 != 0:
        cont += 1

print("total: ", cont)
