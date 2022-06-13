class CodeNotFound(Exception):
    """ Artista não encontrado """
    pass


try:
    raise CodeNotFound('Erro ao encontrar um artista')

except CodeNotFound as error:
    print(error)
