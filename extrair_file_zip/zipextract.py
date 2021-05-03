from zipfile import ZipFile

# instanciando obj e arquivo
file = ZipFile('arquivo_zip.zip')

# Escolha o path para os arquivos
file.extractall(path='')