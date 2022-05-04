import os
import pathlib

# os
print(os.getcwd())
print(os.path.abspath(os.getcwd()))
print(os.path.dirname(os.path.realpath(__file__)))

# pathlib
print(pathlib.Path().absolute())
print(pathlib.Path(__file__).parent.absolute())

# Todos com a mesma saída
# C:\Sample\Python
