from collections import defaultdict
import sys
lines = sys.stdin.read().split("\n")

graph = {}
flows = []
node_to_flow = {}
for line in lines:
    line = line.replace(",", "")
    data = line.split()
    node = data[1]
    flow = int(data[4][5:-1])
    go_to = data[9:]

    graph[node] = go_to
    flows.append((flow, node))
    node_to_flow[node] = flow

flows.sort(reverse=False)
# print(graph)

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
    # print_solution(distance)
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

dp = [[0, 0,["AA"]] for _ in range(30)]

import random
random.shuffle(flows)
print(flows)

# flows = [(0, 'AA'), (20, 'DD'), (2, 'CC'), (13, 'BB')]
# flows = [(0, 'AA'),(2, 'CC'), (13, 'BB'), (20, 'DD')  ]
seen = set()
for flow, n in flows:
    seen.add(n)
    if n == "AA":
        continue

    for i in range(1, 30):
        prev = dp[i-1].copy()
        prev[0] += prev[1]

        if prev[0] > dp[i][0]:
            dp[i] = prev


        # print(i, dp[i])
        # Increment
        for s in seen:
            if s not in dp[i][2]:

                for j in range(i-1, -1, -1):
                    # print(j)
                    last = dp[j][2][-1]
                    distance = G[node_to_idx[s]][node_to_idx[last]] + 1
                    # print(">>",s, last, distance)
                    if j + distance == i:
                        if s not in dp[i - distance][2]:
                            x = dp[i - distance].copy()
                            x[0] += x[1]*distance
                            x[0] += node_to_flow[s]
                            x[1] += node_to_flow[s]
                            x[2] = x[2].copy()
                            x[2].append(s)

                            if x[0] > dp[i][0]:
                                # print(x, j)
                                # print(distance, s, last, j)
                                dp[i] = x


numbers = []
for x in dp:
    numbers.append(x[0])
print(dp)
print(numbers)

# for i in range(1, len(numbers)):
#     print(i, numbers[i]-numbers[i-1])
