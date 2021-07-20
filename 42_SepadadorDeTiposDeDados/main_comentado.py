lista = [[1, 2, 3], 'Python', 1, 1.2, [4, 5], 2, 'C++', 3.5]
dicio = {}

# A list comprehension transforma todos os dados em seus tipos
tipos = [type(item) for item in lista]

# Percorre um set com cada tipo de dado
for tipo in set(tipos):
    lista_tipo = []
    # Percorre a lista com os itens
    for item in lista:
        # Se o tipo do dado for igual ao tipo da vez
        if type(item) == tipo:
            # Armazena dentro da lista_tipo
            lista_tipo.append(item)

    # Fatia o retorno da string para exibir apenas o tipo
    nome_tipo = str(tipo)[8:][:-2]
    # Cria uma chave com a variavel nome tipo e salva a lista com todos dados de tipos iguals
    dicio[nome_tipo] = lista_tipo

print(dicio)

# [Saída]:
# {'int': [1, 2], 'str': ['Python', 'C++'], 'float': [1.2, 3.5], 'list': [[1, 2, 3], [4, 5]]}
