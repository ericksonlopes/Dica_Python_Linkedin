items = ['Maça', 'Banana', 'Grapes']

for index, value in enumerate(items, 1):
    print(index, value, sep='-')


print(list(enumerate(items, start=1)))
