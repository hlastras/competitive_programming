def maxValue(n, rounds):
    store = [[1, n, 0]]
    for round in rounds:
      l, r, c = round
      for i in range(l-1, r):
        counts[i] += c

    return max(counts)

if __name__ == '__main__':
    n = int(input().strip())

    rounds_rows = int(input().strip())
    rounds_columns = int(input().strip())

    rounds = []

    for _ in range(rounds_rows):
        rounds.append(list(map(int, input().rstrip().split())))

    print(maxValue(n, rounds))