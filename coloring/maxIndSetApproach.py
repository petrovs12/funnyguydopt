__author__ = 'stefan'
import networkx as nx
from networkx.algorithms.approximation import clique_removal,maximum_independent_set,min_maximal_matching,vertex_cover
graphEdges=[ (0 ,16),
    (1, 2),
(1, 6),
(1, 7),
(1, 8),
(2, 11),
(2, 16),
(2, 17),
(3, 14),
(3, 16),
(3, 17),
(4, 7),
(4, 13),
(4, 17),
(5, 6),
(5, 11),
(6 ,18),
(9 ,12),
(10, 13),
(11, 17),
(13, 15),
(15 ,17),
(16 ,19)]
graph=nx.Graph()

graph.add_edges_from(graphEdges)
print(graph.nodes())
print(graph.edges())
print(min_maximal_matching(graph))
print(graph)

g1=nx.barabasi_albert_graph(1000,400)
print(nx.maximal_independent_set((g1)))
solution=[-1]*g1