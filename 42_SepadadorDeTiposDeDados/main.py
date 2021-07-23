lista = [[1, 2, 3], 'Python', 1, 1.2, [4, 5], 2, 'C++', 3.5]
dicio = {}

for tipo in set([type(item) for item in lista]):
    lista_tipo = [item for item in lista if tipo == type(item)]
    dicio[str(tipo)[8:][:-2]] = lista_tipo

print(dicio)

# [Saída]:
# {'int': [1, 2], 'str': ['Python', 'C++'], 'float': [1.2, 3.5], 'list': [[1, 2, 3], [4, 5]]}
