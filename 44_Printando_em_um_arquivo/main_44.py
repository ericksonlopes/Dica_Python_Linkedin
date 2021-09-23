# Exemplo 1
print("Esta dica é muito interessante!", file=open("arquivo.txt", "w"))

# Exemplo 2
with open("arquivo.txt", "a") as arquivo_with:
    print("Adicionando mais texto!", file=arquivo_with)

# Exemplo 3
arquivo = open("arquivo.txt", "a")
print("Isso é python !", file=arquivo)



