from collections import namedtuple

# Criando estrutura
DicaPython = namedtuple("DicaPython", ["numero_dica", "texto"])

# Criando instancia e adicionando o valor
nova_dica = DicaPython("60", "Criando estrutura de dados imutável.")

print(nova_dica.numero_dica)
# 60

print(nova_dica.texto)
# Criando estrutura de dados imutável.
