# Exemplo 1 ------------------------------------

# função lambda para multiplicação
x = lambda a, b: a * b
print(x(5, 6))
# 30

# Exemplo 2 ------------------------------------

# Criando lista
items = range(1, 8)

# Função lambda que multiplica cada número por 2
mult_dois = list(map(lambda var: var*2, items))

print(mult_dois)
# [2, 4, 6, 8, 10, 12, 14]
