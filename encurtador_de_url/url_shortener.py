# pip install pyshorteners


import pyshorteners

url = 'https://pyshorteners.readthedocs.io/en/latest/'

s = pyshorteners.Shortener()

print('Sua url incurtada: ', s.tinyurl.short(url))

# https://pypi.org/project/pyshorteners/
# Uma biblioteca Python do wrapper de API de encurtamento de URL simples.
