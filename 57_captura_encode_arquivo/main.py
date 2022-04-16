# pip install chardet
import chardet

with open("arquivo.log", 'rb') as file:
    # Ler conteudo
    data = file.read()

    # Detectar encoding
    enc = chardet.detect(data)

    # Imprimindo enconding
    print(enc['encoding'])
    # "utf-8"

    # Decodifica os bytes no encode encontrado
    print(data.decode(enc['encoding']))
    # {ãáã}
