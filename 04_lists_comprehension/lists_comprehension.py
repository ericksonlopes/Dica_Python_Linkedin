frutas = ['maça', 'banana', 'cherry', 'manga']

# criando lista varia para adicionar itens
lista_loop = []
# Percorrendo lista com o loop for
for fruta in frutas:
    # adicionando item dentro dalista
    lista_loop.append(fruta)

print(lista_loop)  # ['maça', 'banana', 'cherry', 'manga']


# A variavel recebe uma lista
lista_comp = [fruta for fruta in frutas]

print(lista_comp)
