from numpy import random
from networkx.generators.random_graphs import erdos_renyi_graph
from matplotlib import pyplot as plt

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

plt.xlim(-10, 110)
plt.ylim(-10, 110)
plt.plot([x[0] for x in graph], [x[1] for x in graph], color='green', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12)
# plt.show()
