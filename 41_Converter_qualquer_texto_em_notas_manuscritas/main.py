# Instalar bibliotec
# >>> pip install pywhatkit

import pywhatkit

var = """
Python é uma linguagem de programação de alto
nivel, interpretada de script, imperativa, orientada a
objetos, funcional, de tipagem dinamica e forte. Foi
lançada por Guido van Rossum em 1991
"""

pywhatkit.text_to_handwriting(var, rgb=[0, 0, 255])
