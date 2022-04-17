from itertools import cycle

lista = [10, 20, 30]
numeros = cycle(lista)

for _ in range(5):
    print(next(numeros))

    # 10
    # 20
    # 30
    # 10
    # 20
