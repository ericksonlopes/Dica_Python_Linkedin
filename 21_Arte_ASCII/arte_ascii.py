# instalar biblioteca
# pip install pyfiglet

import pyfiglet

# string que sera renderizada
word = 'Python'

# Com o módulo pyfiglet.print_figlet para exibir no terminal,
# especificando a str que sera renderizada e o tipo de font
pyfiglet.print_figlet(word, font='digital')
pyfiglet.print_figlet(word, font='stop')

# o trecho retorna todas as fontes disponiveis
all_fonts = pyfiglet.FigletFont.getFonts()
