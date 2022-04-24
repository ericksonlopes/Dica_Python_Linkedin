lista = ['primeiro-item', 'segundo-item', 'terceiro-item']

for idade, nome in enumerate(lista, 70):
    print(f'{nome:>13} ', idade)

# primeiro-item  70
#  segundo-item  71
# terceiro-item  72