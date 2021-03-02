# instalar biblioteca
# pip install pyfiglet

import pyfiglet

word = 'Python'

data_figlet = pyfiglet.figlet_format(word)

data_font = pyfiglet.print_figlet(word, font='digital')

# print(data_figlet)
# print(data_font)
# print()

for item in pyfiglet.FigletFont.getFonts():
    print(item)
    print(pyfiglet.print_figlet(word, font=item), '\n')