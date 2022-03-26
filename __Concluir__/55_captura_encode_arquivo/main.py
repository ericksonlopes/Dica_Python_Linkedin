import chardet

with open("arquivo.log", 'rb') as file:
    data = file.read()
    enc = chardet.detect(data)
    print(data.decode(enc['encoding']))
