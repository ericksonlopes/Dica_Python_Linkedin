# importe a biblioteca
import csv

# Abre/cria o arquivo no modo leitura
arquivo = open('arquivo.csv', 'w', newline='')

# informa para o csv qual arquivio vai ser escrito
escrever = csv.writer(arquivo)

# Escrevendo no arquivo
escrever.writerow(['Erickson', '18', 'Engenheiro de dados'])
escrever.writerow(['Paulo', '25', 'Cientista de dados'])
escrever.writerow(['Jackson', '21', 'Full stack'])

# quando finalizar as alterações, feche o arquivo
arquivo.close()
