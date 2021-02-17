# Instalar biblioteca
# pip install pyinputplus

from pyinputplus import inputNum, inputURL, inputEmail

# Aceita uma string
email = inputEmail(prompt='Digite seu email: ')
# Digite seu email: erickson@gmail.com

# Aceita apenas uma string no formato de url, retornando a string
url = inputURL(prompt='Digite uma url: ')
# Digite uma url: erickson.com.br

# Aceita apenas um número inteiro, Retornando um int, não um str.
num = inputNum(prompt='Digite um número: ')
# Digite um número: 369


# OUTROS TESTES
# MENU
# variavel = inputMenu(['Cachorro', 'Gato', 'Boi'])
# variavel = inputMenu(['Cachorro', 'Gato', 'Boi'], numbered=True)
# variavel = inputMenu(['Cachorro', 'Gato', 'Boi'], lettered=True)

# NUMERO
# variavel = inputNum('Digite um número: ')
# variavel = inputNum('Digite um número: ', max=9)

# CHOICES
# variavel = inputChoice(['1', '2'])
# try:
#     variavel = inputChoice(['1', '2'], limit=2)
# except RetryLimitException:
#     print('Acabou suas chances')
# else:
#     print(variavel)


# URL
# variavel = inputURL(prompt='Digite  url que deseja encontrar: ')


# print(variavel)

