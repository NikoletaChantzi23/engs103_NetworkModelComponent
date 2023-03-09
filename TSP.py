###############################
######  Nikoleta Chantzi ######
#####  Network Component  #####
#### FinalProject|ENGS103  ####
###############################

## Run these on your terminal before proceeding
# pip install networkx
# pip install python-tsp
import numpy as np
from matplotlib import pyplot as plt
from python_tsp.exact import solve_tsp_dynamic_programming, solve_tsp_brute_force
from python_tsp.heuristics import solve_tsp_simulated_annealing
import networkx as nx


# Solving TSP
distance_matrix = np.loadtxt("/Users/nikoletachantzi/Library/CloudStorage/OneDrive-DartmouthCollege/WINTER "
                             "2023/ENGS103/finalProject/Network Problem-BigNumbers.csv",delimiter=",")
permutation, distance = solve_tsp_dynamic_programming(distance_matrix)
print(permutation)
print(distance)

permutation, distance = solve_tsp_simulated_annealing(distance_matrix)
print(permutation)
print(distance)


## Network for MST; Prim's Algo
g = nx.Graph()

g.add_edge(1, 6, weight=186)
g.add_edge(6, 11, weight=162)
g.add_edge(6, 7, weight=220)
g.add_edge(1, 2, weight=279)
g.add_edge(2, 3, weight=247)
g.add_edge(3, 4, weight=230)
g.add_edge(4, 10, weight=279)
g.add_edge(6, 5, weight=452)
g.add_edge(5, 9, weight=526)
g.add_edge(9, 8, weight=301)
g.add_edge(2, 16, weight=529)
g.add_edge(16, 13, weight=217)
g.add_edge(16, 12, weight=395)
g.add_edge(12, 15, weight=475)
g.add_edge(13, 17, weight=708)
g.add_edge(3, 18, weight=1270)
g.add_edge(13, 14, weight=1330)

pos = nx.spring_layout(g)
labels = nx.get_edge_attributes(g,'weight')
plt.figure(figsize=(25,8))
nx.draw(g, pos=pos, alpha=0.5)
nx.draw_networkx_edge_labels(g, pos=pos, edge_labels=labels, alpha=0.5)
nx.draw_networkx_labels(g, pos=pos, alpha=1)
plt.savefig("Dijkstra's.png")


## Network for TSP option A
g = nx.Graph()
g.add_edge(0, 15, weight=3470)
g.add_edge(15, 12, weight=475)
g.add_edge(12, 16, weight=395)
g.add_edge(16, 2, weight=529)
g.add_edge(2, 1, weight=279)
g.add_edge(1, 7, weight=385)
g.add_edge(7, 6, weight=220)
g.add_edge(6, 11, weight=162)
g.add_edge(11, 8, weight=771)
g.add_edge(8, 9, weight=301)
g.add_edge(9, 5, weight=526)
g.add_edge(5, 3, weight=805)
g.add_edge(3, 4, weight=230)
g.add_edge(4, 10, weight=279)
g.add_edge(10, 14, weight=1780)
g.add_edge(14, 13, weight=1330)
g.add_edge(13, 17, weight=708)
g.add_edge(17, 18, weight=1640)

pos = nx.spring_layout(g)
labels = nx.get_edge_attributes(g,'weight')
plt.figure(figsize=(25,12))
nx.draw(g, pos=pos, alpha=0.5)
nx.draw_networkx_edge_labels(g, pos=pos, edge_labels=labels, alpha=0.5)
nx.draw_networkx_labels(g, pos=pos, alpha=1)
plt.savefig("TSP_OptionA.png")

## Network for TSP option B
g = nx.Graph()
g.add_edge(0, 18, weight=2790)
g.add_edge(18, 14, weight=2600)
g.add_edge(14, 10, weight=1780)
g.add_edge(10, 4, weight=279)
g.add_edge(4, 3, weight=230)
g.add_edge(3, 2, weight=247)
g.add_edge(2, 1, weight=279)
g.add_edge(1, 7, weight=385)
g.add_edge(7, 6, weight=220)
g.add_edge(6, 5, weight=452)
g.add_edge(5, 9, weight=526)
g.add_edge(9, 8, weight=301)
g.add_edge(8, 11, weight=771)
g.add_edge(11, 15, weight=775)
g.add_edge(15, 12, weight=475)
g.add_edge(12, 16, weight=395)
g.add_edge(16, 13, weight=217)
g.add_edge(13, 17, weight=708)

pos = nx.spring_layout(g)
labels = nx.get_edge_attributes(g,'weight')
plt.figure(figsize=(25,12))
nx.draw(g, pos=pos, alpha=0.5)
nx.draw_networkx_edge_labels(g, pos=pos, edge_labels=labels, alpha=0.5)
nx.draw_networkx_labels(g, pos=pos, alpha=1)
plt.savefig("TSP_OptionB.png")