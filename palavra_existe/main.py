with open('arquivo.txt') as arquivo:
    data = arquivo.read()
    palavra = 'Python'

    if palavra in data:
        print('Existe a palavra')
    else:
        print('Não existe a palavra')