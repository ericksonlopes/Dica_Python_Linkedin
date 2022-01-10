from functools import partial

# Congelando um print para que termine com uma vírgula em vez de uma nova linha
new_print = partial(print, end=', ')

for _ in range(5):
    new_print('-')

# [SAÍDA]
# -, -, -, -, -,


# Congelando um enumerate para começar a contagem pelo index igual a 2
new_enumerate = partial(enumerate, start=2)

for var in new_enumerate(range(5)):
    print(var)

# [SAÍDA]
# (3, 1)
# (4, 2)
# (5, 3)
# (6, 4)