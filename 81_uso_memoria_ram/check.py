"""
verificar o uso de memória de um objeto

:Autor: Erickson Lopes
"""

import sys

string = '1'
print(sys.getsizeof(string))
# 50

inteiro = 1
print(sys.getsizeof(inteiro))
# 28

dicio = {}
print(sys.getsizeof(dicio))
# 64
