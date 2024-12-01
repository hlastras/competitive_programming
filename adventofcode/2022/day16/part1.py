from collections import defaultdict
import sys
lines = sys.stdin.read().split("\n")

graph = {}
flows = []
for line in lines:
    line = line.replace(",", "")
    data = line.split()
    node = data[1]
    flow = int(data[4][5:-1])
    go_to = data[9:]

    graph[node] = go_to
    flows.append((flow, node))

flows.sort(reverse=False)
# print(flows)
print(graph)

nodes = list(graph.keys())
nodes.sort()
node_to_idx = {}
for i, n in enumerate(nodes):
    node_to_idx[n] = i


# Calcular matriz de distancias
# Floyd Warshall Algorithm in python


# The number of vertices
nV = len(graph)
INF = 9999999999


# Algorithm implementation
def floyd_warshall(G):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))

    # Adding vertices individually
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    print_solution(distance)
    return distance


# Printing the solution
def print_solution(distance):
    for i in range(nV):
        for j in range(nV):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")


G = [[INF] * nV for _ in range(nV)]

for n in nodes:
    idx = node_to_idx[n]
    G[idx][idx] = 0
    for next in graph[n]:
        idx2 = node_to_idx[next]
        G[idx][idx2] = 1
        G[idx2][idx] = 1

G = floyd_warshall(G)




####################################### PART 3

dp = [[[0,["AA"]] for _ in range(31)]]

for flow, n in flows:
    if n == "AA":
        continue

    print(n)

    new_row = []
    for i in range(31):
        validate = [dp[-1][i]]
        for j in range(i-1, -1, -1):
            letra = dp[-1][j][1][-1]
            idx_letra = node_to_idx[letra]
            idx = node_to_idx[n]
            distancia = G[idx][idx_letra] + 1

            if j+distancia == i:
                # print("VALIDO", letra, n, i, j, distancia)
                item = dp[-1][j]
                nl = item[1].copy()
                nl.append(n)
                new_item = [item[0]+flow, nl]
                validate.append(new_item)
        # print(validate)
        validate.sort(reverse=True)
        print(validate[0])
        new_row.append(validate[0])

    dp.append(new_row)




for row in dp:
    print(row)