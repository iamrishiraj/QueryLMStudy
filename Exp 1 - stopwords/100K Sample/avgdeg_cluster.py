import networkx as nx
import sys

g=nx.Graph()
edge=[]
edge.append((1,2))
edge.append((2,3))
edge.append((3,4))
edge.append((3,5))
edge.append((6,7))
g.add_edges_from(edge)
h=list(nx.connected_component_subgraphs(g))[0]

print h.edges()

    
