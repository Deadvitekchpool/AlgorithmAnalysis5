from numpy import random
from networkx.generators.random_graphs import erdos_renyi_graph
from matplotlib import pyplot as plt
from igraph import *

graph = erdos_renyi_graph(100, 0.05)

graph = list(graph.edges)[:200]
matrix = [[0 for _ in range(100)] for _ in range(100)]

for x, y in graph:
	matrix[x][y] = 1
	matrix[y][x] = 1

difference = 400

for i, row in enumerate(matrix):
	if sum(row) == 0:
		temp = random.randint(0, 99)
		row[temp] = 1
		matrix[temp][i] = 1
		difference += 2
		graph.append((i, temp))


x = len(graph) - 200
while difference > 400:
	for j in range(len(matrix)):
		if sum(matrix[j]) == 6 + x:
			flag = x % 2
			for i in range(x):
				matrix[j] = list(reversed(matrix[j]))
				one_to_del = matrix[j].index(1)
				matrix[j][one_to_del] = 0
				if i + 1 % 2 != 0:
					matrix[99 - one_to_del][j] = 0
				else:
					matrix[one_to_del][j] = 0
				difference -= 2
				
				graph = list(reversed(graph))
				for pair in graph:
					if pair[0] == j:
						graph.remove(pair)
						break

			if flag:
				matrix[j] = list(reversed(matrix[j]))
				graph = list(reversed(graph))
			if difference == 400:
				break

g = Graph()
g.add_vertices(100)
g.add_edges(graph)
layout = g.layout("kamada_kawai")
fig, ax = plt.subplots()
plot(g, layout=layout, bbox=(300, 300), margin=20, target=ax)
plt.show()
