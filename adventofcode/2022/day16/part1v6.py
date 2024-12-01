import sys
from heapq import heappush, heappop

def parse_input(file):
    graph = {}
    flow_rates = {}
    for line in file:
        parts = line.strip().split('; ')
        valve_info, tunnel_info = parts[0], parts[-1]
        valve, rate = valve_info.split(' has flow rate=')
        flow_rates[valve] = int(rate)

        if 'lead to valves' in tunnel_info:
            connections = tunnel_info.split(' lead to valves ')[1].split(', ')
            graph[valve] = connections
        else:
            graph[valve] = []

    if 'AA' not in graph:
        graph['AA'] = []  # Ensure 'AA' is always present

    return graph, flow_rates

def find_max_pressure(graph, flow_rates):
    max_time = 30
    best_pressure = 0
    queue = [(-0, 'AA', 0, set())]  # Initial state

    while queue:
        pressure, current_valve, time, visited = heappop(queue)
        pressure = -pressure

        if time >= max_time:
            best_pressure = max(best_pressure, pressure)
            continue

        for next_valve in graph.get(current_valve, []):  # Safe access to graph
            if next_valve not in visited:
                new_visited = visited.copy()
                new_visited.add(next_valve)
                new_pressure = pressure + (max_time - time - 1) * flow_rates[next_valve]
                heappush(queue, (-new_pressure, next_valve, time + 2, new_visited))

    return best_pressure

if __name__ == "__main__":
    graph, flow_rates = parse_input(sys.stdin)
    max_pressure = find_max_pressure(graph, flow_rates)
    print(max_pressure)
