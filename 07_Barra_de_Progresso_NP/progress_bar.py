# importe as bibliotecas
from time import sleep
from tqdm import tqdm

# coloque dentro da função tqdm o iteravel a ser utilizado
for cont in tqdm(range(30), desc='Contador 1'):
    # sleep para cada vez no loop ter 30s
    sleep(0.30)

# utilizando list comprehension
[sleep(0.30) for var in tqdm(range(30), desc='Contador 2')]
