# 8) Entre os números 2345 e 8764 quantos são impares?

cont = 0
for i in range(2345, 8765):
    if i % 2 != 0:
        cont += 1

print("total: ", cont)
