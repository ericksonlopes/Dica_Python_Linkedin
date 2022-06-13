# pip install rich

from rich import print
from rich.tree import Tree

tree = Tree('[cyan]Dicas Python')
tree.add('[red]73.py')
tree.add('[blue]trab.json')

src = tree.add('[cyan]Sub dicas')
src.add('[red]main.py')

print(tree)

# Dicas Python
# ├── data.py
# ├── trab.json
# └── Sub dicas
#     └── main.py
