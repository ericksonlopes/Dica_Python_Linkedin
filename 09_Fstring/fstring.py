## Interaveis

name = 'Python'

print(f'{name:.1}')
# p

print(f'{name:.3}')
# Pyt

print(f'{name:.{len(name)}}')

## Passando um inteiro após o ':' fará com que o campo tenha um número mínimo de caracteres de largura.

print(f'O Erickson é um {"Programador":^30} Python')
# O Erickson é um          Programador           Python


## Alinhamento, com a quantidade de caractere fornecido

print(f'[{name:>10}]')
# [    Python]

print(f'[{name:<10}]')
# [Python    ]

print(f'[{name:^10}]')
# [  Python  ]


## Um especificador opcional de formato pode ser incluído após a expressão.
# Isso permite maior controle sobre como o valor é formatado

num = 10

print(f'{num:.1f}')
# 10.0

print(f'{num:.2f}')
# 10.00

print(f'{num:.3f}')
# 10.000
