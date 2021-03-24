lista = [1, ]

lista += [2]
# [1, 2]

lista = lista + [3, 4, 5]
# [1, 2, 3, 4, 5]

lista.append(6)
# [1, 2, 3, 4, 5, 6]

lista_2 = [7, 8, 9]
lista.extend(lista_2)  # concatena as listas
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

lista.insert(len(lista), 10)  # (posição, valor)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_3 = [11, 12]
lista = [*lista, *lista_3]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(lista)
