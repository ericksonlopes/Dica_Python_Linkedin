# instalar biblioteca(pip)
# pip install Faker

from faker import Faker

# Instanciando classe utilizada e configurando para pt-br
fake = Faker('pt_br')

print(fake.name(), '\n')
# Ana Lívia Pereira

print(fake.address())
# Ladeira Gonçalves, 90
# Cenaculo
# 81515-427 Castro da Mata / DF

print(fake.email())
# abarros@hotmail.com

print(fake.text())
# Culpa dicta veniam ipsum vero atque. Voluptatem animi natus et
# reprehenderit iusto perspiciatis. Eum enim consequuntur placeat beatae.

print(fake.phone_number())
# +55 (084) 3092-1293
