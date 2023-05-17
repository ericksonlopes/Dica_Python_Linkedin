import networkx as nx
import matplotlib.pyplot as plt

# Cria um grafo vazio
G = nx.Graph()

# Adiciona nós
G.add_node("Erickson")
G.add_node("Lopes")


# Adiciona arestas
G.add_edge("Erickson", "Lopes")


# Visualiza o grafo
nx.draw(G, with_labels=True)
plt.show()
