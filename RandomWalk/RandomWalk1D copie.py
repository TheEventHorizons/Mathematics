import numpy as np
import matplotlib.pyplot as plt

# Paramètres de la simulation
num_steps = 1000  # Nombre d'étapes
step_size = 1  # Taille d'une étape

# Générer les étapes aléatoires
random_steps = np.random.choice([-1, 1], size=num_steps)
random_walk = np.cumsum(random_steps * step_size)

# Tracer le random walk
plt.plot(random_walk)
plt.title('Simulation d\'une Random Walk à une dimension')
plt.xlabel('Nombre d\'étapes')
plt.ylabel('Position')
plt.grid(ls='--')
plt.show()

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Définition des états
etats = ['A', 'B', 'C']

# Matrice de transition
matrice_transition = np.array([[0.3, 0.7, 0.0],
                               [0.2, 0.0, 0.8],
                               [0.5, 0.5, 0.0]])

# Création d'un graphe dirigé
G = nx.DiGraph()

# Ajout des états en tant que nœuds
G.add_nodes_from(etats)

# Ajout des arêtes avec les poids de la matrice de transition
for i, origine in enumerate(etats):
    for j, destination in enumerate(etats):
        poids_transition = matrice_transition[i, j]
        if poids_transition > 0:
            G.add_edge(origine, destination, weight=poids_transition)

# Affichage du graphe
pos = nx.circular_layout(G)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_nodes(G, pos, node_size=300, node_color='lightblue')
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title('Chaîne de Markov')
plt.show()
