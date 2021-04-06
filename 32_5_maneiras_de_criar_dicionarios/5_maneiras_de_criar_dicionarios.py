"""
5 Maneiras de criar dicionários

"""

dicio_1 = dict(primeiro=1, segundo=2, terceiro=3)
# {'primeiro': 1, 'segundo': 2, 'terceiro': 3}

dicio_2 = {'primeiro': 1, 'segundo':  2, 'terceiro': 3}
# {'primeiro': 1, 'segundo': 2, 'terceiro': 3}

dicio_3 = dict(zip(['primeiro', 'segundo', 'terceiro'], [1, 2, 3]))
# {'primeiro': 1, 'segundo': 2, 'terceiro': 3}

dicio_4 = dict([('primeiro', 1), ('segundo', 2), ('terceiro', 3)])
# {'primeiro': 1, 'segundo': 2, 'terceiro': 3}

dicio_5 = dict({'primeiro': 1, 'segundo':  2, 'terceiro': 3})
# {'primeiro': 1, 'segundo': 2, 'terceiro': 3}

print(dicio_1)
print(dicio_2)
print(dicio_3)
print(dicio_4)
print(dicio_5)
