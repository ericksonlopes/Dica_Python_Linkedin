# pip install pyttsx3

import pyttsx3

# carrega a lib
engine = pyttsx3.init()

# Declarando o que a lib vai falar
engine.say('Olá mundo')
engine.say('Trago conteúdo de segunda a sexta para vocês !!')

# Executa
engine.runAndWait()

# pyttsx3 é uma biblioteca de conversão de texto em fala em Python.
# Ao contrário das bibliotecas alternativas, ele funciona offline e é compatível com Python 2 e 3.