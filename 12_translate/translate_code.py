# Instalar biblioteca
# pip install translate

from translate import Translator

# configurando tradução
conf = Translator(from_lang='english', to_lang='pt-br')

# Especificando texto a ser traduzido
result = conf.translate('Hello World')

print(result)
# Saida: Olá Mundo
