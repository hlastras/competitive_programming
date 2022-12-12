import sys
lines = sys.stdin.read().split("\n")

digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

def vaule_or_variable(input):
    if input[0] in digits:
        return int(input)
    return input

def parse(input):
    x = input.split()

    if len(x) == 3:
        action = x[1]
        v1 = vaule_or_variable(x[0])
        v2 = vaule_or_variable(x[2])
        return [action, v1, v2]
    
    if len(x) == 2:
        # Is a NOT
        action = x[0]
        v1 = vaule_or_variable(x[1])
        return [action, v1, None]

    if len(x) == 1:
        return ["COPY", vaule_or_variable(x[0]), None]

input_value = None

for _ in range(2):
    graph = {}
    nodes = [None] * len(lines)
    for i, line in enumerate(lines):
        left, right = line.split(" -> ")

        if right not in graph:
            graph[right] = [None, []]
        graph[right][0] = i

        node = [None, None, None, None]
        a, v1, v2 = parse(left)
        node[0] = a
        if type(v1) == int:
            node[1] = v1
        else:
            if v1 not in graph:
                graph[v1] = [None, []]
            graph[v1][1].append(i)
        if type(v2) == int:
            node[2] = v2
        else:
            if v2 not in graph:
                graph[v2] = [None, []]
            graph[v2][1].append(i)
        nodes[i] = node

    if input_value != None:
        nodes[graph['b'][0]][1] = input_value
        
    graph2 = {}
    for k, v in graph.items():
        graph2[v[0]] = v[1]

    queue = []
    for i, node in enumerate(nodes):
        if node[0] == "COPY" and type(node[1]) == int:
            queue.append(i)

    while len(queue) > 0:
        idx = queue[0]
        node = nodes[idx]
        queue = queue[1:]

        if node[3] != None:
            continue

        if node[0] == "AND" and node[1] != None and node[2] != None:
            value = node[1] & node[2]
            node[3] = value
            for i in graph2[idx]:
                if nodes[i][1] == None:
                    nodes[i][1] = node[3]
                else:
                    nodes[i][2] = node[3]
                queue.append(i)
        
        if node[0] == "OR" and node[1] != None and node[2] != None:
            value = node[1] | node[2]
            node[3] = value
            for i in graph2[idx]:
                if nodes[i][1] == None:
                    nodes[i][1] = node[3]
                else:
                    nodes[i][2] = node[3]
                queue.append(i)

        if node[0] == "LSHIFT" and node[1] != None and node[2] != None:
            value = node[1] << node[2]
            node[3] = value
            for i in graph2[idx]:
                if nodes[i][1] == None:
                    nodes[i][1] = node[3]
                else:
                    nodes[i][2] = node[3]
                queue.append(i)

        if node[0] == "RSHIFT" and node[1] != None and node[2] != None:
            value = node[1] >> node[2]
            node[3] = value
            for i in graph2[idx]:
                if nodes[i][1] == None:
                    nodes[i][1] = node[3]
                else:
                    nodes[i][2] = node[3]
                queue.append(i)
                
        if node[0] == "NOT" and node[1] != None:
            value = ~node[1]
            node[3] = value
            for i in graph2[idx]:
                if nodes[i][1] == None:
                    nodes[i][1] = node[3]
                else:
                    nodes[i][2] = node[3]
                queue.append(i)

        if node[0] == "COPY" and node[1] != None:
            value = node[1]
            node[3] = value
            
            for i in graph2[idx]:
                if nodes[i][1] == None:
                    nodes[i][1] = node[3]
                else:
                    nodes[i][2] = node[3]
                queue.append(i)

    input_value = nodes[graph['a'][0]][3]
    print(input_value)