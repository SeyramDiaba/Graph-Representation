# Assignment 1: Graph Representation of Research Group
# Social Networks and Graph Analysis

import networkx as nx
import matplotlib.pyplot as plt

# Create a simple graph of my research group
G = nx.Graph()

# Add nodes (people in the group)
people = ['Stephen', 'Lydia', 'Daniel', 'Prince', 'Charles', 'Samuel', 'Princilla', 'Yeboah','Dr Ansah','Phillip','Adiboye','Raphael']
G.add_nodes_from(people)

# Add edges (who works together)
collaborations = [
    ('Stephen', 'Phillip'),
    ('Lydia', 'Princilla'),
    ('Daniel', 'Prince'),
    ('Samuel', 'Charles'),
    ('Stephen', 'Lydia'),
    ('Yeboah', 'Adiboye'),
    ('Lydia', 'Raphael'),
    ('Dr Ansah', 'Lydia'),
    ('Dr Ansah', 'Daniel'),
    ('Dr Ansah', 'Stephen'),
    ('Dr Ansah', 'Prince'),
    ('Dr Ansah', 'Charles'),
    ('Dr Ansah', 'Samuel'),
    ('Dr Ansah', 'Princilla'),
    ('Dr Ansah', 'Yeboah'),
    ('Dr Ansah', 'Phillip'),
    ('Dr Ansah', 'Adiboye'),
    ('Dr Ansah', 'Raphael'),
    ('Princilla', 'Stephen'),
    ('Princilla', 'Lydia'),
    ('Princilla', 'Daniel'),
    ('Princilla', 'Prince'),
    ('Princilla', 'Charles'),
    ('Princilla', 'Samuel'),
    ('Princilla', 'Yeboah'),
    ('Princilla', 'Phillip'),
    ('Princilla', 'Adiboye'),
    ('Princilla', 'Raphael')
]
G.add_edges_from(collaborations)

# Calculate basic metrics
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()

print("=== Graph Metrics ===")
print(f"Number of nodes: {num_nodes}")
print(f"Number of edges: {num_edges}")

# Degree distribution
print("\n=== Degree Distribution ===")
for person in people:
    connections = len(list(G.neighbors(person)))
    print(f"{person}: {connections} connections")

# Check for isolated nodes
isolated = list(nx.isolates(G))
print(f"\n=== Isolated Nodes ===")
if isolated:
    print(f"Isolated nodes: {isolated}")
else:
    print("No isolated nodes")

# Visualize the network
fig, ax = plt.subplots(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color='lightblue', 
        node_size=1000, font_size=12, font_weight='bold', ax=ax)
ax.set_title("Research Group Network")
plt.savefig('network.png')
plt.show()

print("\nGraph saved as 'network.png'")
