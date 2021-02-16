# Instalar biblioteca
# pip install pyinputplus

from pyinputplus import inputIp, inputMenu, inputNum, inputChoice, RetryLimitException, inputURL

# MENU
# variavel = inputMenu(['Cachorro', 'Gato', 'Boi'])
# variavel = inputMenu(['Cachorro', 'Gato', 'Boi'], numbered=True)
# variavel = inputMenu(['Cachorro', 'Gato', 'Boi'], lettered=True)

# NUMERO
# variavel = inputNum('Digite um número: ')
# variavel = inputNum('Digite um número: ', max=9)

# CHOICES
variavel = inputChoice(['1', '2'])
try:
    variavel = inputChoice(['1', '2'], limit=2)
except RetryLimitException:
    print('Acabou suas chances')
else:
    print(variavel)


# URL
# variavel = inputURL(prompt='Digite  url que deseja encontrar: ')


# print(variavel)

