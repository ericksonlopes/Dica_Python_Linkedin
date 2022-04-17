from collections import Counter
import os
from pathlib import Path


def count_extensions(path='.', top=10):
    cnt = Counter()
    for root, dirs, files in os.walk(path):
        for file in files:
            cnt[Path(file).suffix] += 1
    return cnt.most_common(top)


# path= caminho / top = os 10 com maior quantidade
ret = count_extensions(path=r'C:\Projetos\Dica_Python_Linkedin', top=10)

print(ret)
# [('.py', 3462), ('.pyc', 3332), ('', 451), ('.pyi', 197), ('.txt', 121),
# ('.h', 116), ('.png', 95), ('.afm', 60), ('.pyd', 48), ('.c', 40)]
