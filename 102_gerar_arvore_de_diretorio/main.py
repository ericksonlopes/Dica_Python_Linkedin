import os


def gerar_arvore(diretorio_raiz, nivel=0):
    for nome_arquivo in os.listdir(diretorio_raiz):
        caminho = os.path.join(diretorio_raiz, nome_arquivo)
        if os.path.isfile(caminho):
            print("|   " * nivel + "|-- " + nome_arquivo)
        elif os.path.isdir(caminho):
            print("|   " * nivel + "+-- " + nome_arquivo)
            gerar_arvore(caminho, nivel + 1)


gerar_arvore('.')
