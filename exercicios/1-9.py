# 9) Entre os números 1 e 10000 quantos são multiplos de 7?

cont = 0
for i in range(1, 10000):
    if i % 7 == 0:
        cont += 1

print("total: ", cont)
