from faker import Faker

# Instanciando classe utilizada e configurando para pt-br
fake = Faker('pt_br')

# abre/cria um arquivo
with open('data.csv', 'w', encoding='utf-8') as arquivo:
    # for para que o código seja repetido 20 vezes
    for item in range(20):
        # gera e escreve os dados dentro do arquivo
        arquivo.writelines(f'{fake.name()},{fake.email()},{fake.phone_number()}\n')
