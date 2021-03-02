# instalar biblioteca
# pip install pyshorteners

import pyshorteners

url = 'https://pyshorteners.readthedocs.io/en/latest/'

s = pyshorteners.Shortener()

print('Sua url incurtada: ', s.tinyurl.short(url))
