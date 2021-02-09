# importando instância
from time import sleep
from tqdm import tqdm

for cont in tqdm(range(100), desc='Contador'):
    sleep(0.30)


# Barra de Progresso com python