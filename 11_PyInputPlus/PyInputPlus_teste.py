# Instalar biblioteca
# pip install pyinputplus

from pyinputplus import inputIp, inputMenu, inputNum, inputChoice, RetryLimitException

# MENU
# variavel = inputMenu(['Cachorro', 'Gato', 'Boi'])
# variavel = inputMenu(['Cachorro', 'Gato', 'Boi'], numbered=True)
# variavel = inputMenu(['Cachorro', 'Gato', 'Boi'], lettered=True)

# NUMERO
# variavel = inputNum('Digite um número: ')
# variavel = inputNum('Digite um número: ', max=4)

# CHOICES
# variavel = inputChoice(['1', '2'])

try:
    variavel = inputChoice(['1', '2'], limit=2)
except RetryLimitException:
    print('Acabou suas chances')
else:
    print(variavel)


# class Carro:
#     def __init__(self, carro):
#         self.carro = carro
#
#     def printar_carro(self):
#         print(self.carro)
#
#
# carro = Carro('Fiat Uno')
#
# carro.printar_carro()

