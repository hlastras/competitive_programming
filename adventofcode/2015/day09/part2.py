import itertools
import sys
lines = sys.stdin.read().split("\n")

graph = {}
for line in lines:
    data = line.split()
    f = data[0]
    t = data[2]
    l = int(data[4])

    if f not in graph:
        graph[f] = {}
    if t not in graph:
        graph[t] = {}

    graph[f][t] = l
    graph[t][f] = l


all_paths = itertools.permutations(graph.keys())

shortest_path = []
for path in all_paths:
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += graph[path[i]][path[i + 1]]

    if not shortest_path or total_distance > shortest_path[0]:
        shortest_path = (total_distance, path)

print(shortest_path[0])