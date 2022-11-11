# pip install pipe

from pipe import select

numeros: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtrar os números pares
print(list(numeros | select(lambda x: x % 2 == 0)))
