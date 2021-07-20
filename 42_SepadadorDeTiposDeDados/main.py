lista = [[1, 2, 3], 'Python', 1, 1.2, [4, 5], 2, 'C++', 3.5]
dicio = {}

# A list comprehension gera uma lista com os tipos
tipos = [type(item) for item in lista]

# percorre um set com cada tipo de dado
for tipo in set(tipos):
    lista_tipo = []
    # percorre a lista com os itens
    for item in lista:
        # se o tipo do dado for igual ao tipo da vez
        if type(item) == tipo:
            # armazena dentro da lista_tipo
            lista_tipo.append(item)

    # Fatia o retorno da string para exibir apenas o tipo
    nome_tipo = str(tipo)[8:][:-2]
    # Cria uma chave com o tipo e salva a lista com todos dados de tipo iguais
    dicio[nome_tipo] = lista_tipo

print(dicio)

# [Saída]:
# {'int': [1, 2], 'str': ['Python', 'C++'], 'float': [1.2, 3.5], 'list': [[1, 2, 3], [4, 5]]}





