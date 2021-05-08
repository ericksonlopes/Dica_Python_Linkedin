# $ pip instalar keytotext
from keytotext import pipeline
from translate import Translator

palavras = ['city', 'sky']

# configurando tradução
conf = Translator(from_lang='english', to_lang='pt-br')

# Importando
nlp = pipeline('k2t')

# Rerar frase
frase = nlp(palavras)

# Especificando texto a ser traduzido
result = conf.translate(frase)

print('Palavras-Chaves: ', palavras, '\n')
print('Frase :', frase)
print('Tradução :', result)
