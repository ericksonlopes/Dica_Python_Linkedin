"""
verificar o uso de memória de um objeto

:Autor: Erickson
"""

import sys

x = '1'
print(sys.getsizeof(x))

y = 1
print(sys.getsizeof(y))
