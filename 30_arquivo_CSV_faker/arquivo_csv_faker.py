from faker import Faker

fake = Faker('pt_br')

with open('data.csv', 'w', encoding='utf-8') as arquivo:
    for item in range(20):
        arquivo.writelines(f'{fake.name()},{fake.email()},{fake.phone_number()}\n')
