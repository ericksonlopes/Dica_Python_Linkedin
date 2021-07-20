lista = [[1, 2, 3], 'Python', 1, 1.2, [4, 5], 2, 'C++']

tipos = [type(item) for item in lista]

dicio = {}

for tipo in set(tipos):
    for item in lista:
        if type(item) == tipo:
            print(item)

# print(dicio)




