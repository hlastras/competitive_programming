def maximumContainers(scenarios):
    for scenario in scenarios:
      n, cost, m = [int(x) for x in scenario.split()]
      containers = n // cost
      result = containers
      while containers >= m:
        x = containers // m
        y = containers % m
        containers = x + y
        result += x
      print(result)


if __name__ == '__main__':
    scenarios_count = int(input().strip())

    scenarios = []

    for _ in range(scenarios_count):
        scenarios_item = input()
        scenarios.append(scenarios_item)

    maximumContainers(scenarios)