# 7) Entre os números 1567 e 3763 quantos são pares?

cont = 0
for i in range(1567, 3764):
    if i % 2 == 0:
        cont += 1

print("total: ", cont)
