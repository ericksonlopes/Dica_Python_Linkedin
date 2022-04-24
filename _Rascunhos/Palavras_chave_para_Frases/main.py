# $ pip instalar keytotext
from keytotext import pipeline
from translate import Translator

palavras_pt_br = ['cadeira', 'eu']

# Configurando tradução
plv_conf = Translator(from_lang='pt-br', to_lang='english')
frase_conf = Translator(from_lang='english', to_lang='pt-br')

# traduzindo as palavras para inglês
palavras = [plv_conf.translate(plv) for plv in palavras_pt_br]

# Importando
nlp = pipeline('k2t')

# Gerar frase
frase = nlp(palavras)

# Traduzir a frase para pt-br
result = frase_conf.translate(frase)

print('Palavras-Chaves: ', palavras)
print('Frase :', frase)
print('Frase:', result)

# https://www.linkedin.com/posts/philipvollet_machinelearning-nlp-datascience-activity-6797226874134233088-mEH4
