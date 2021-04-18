fruits = int(input())
weights = [int(x) for x in input().split()]

counts = [2**(len(weights)-1)] * fruits

for i, weight_i in enumerate(weights):
  if weight_i < 200:
    counts[i] -= 1

  for j, weight_j in enumerate(weights[i:], i):
    if i!=j:
      if (weight_i+weight_j) < 200:
        counts[i] -= 1
        counts[j] -= 1
        
    for k, weight_k in enumerate(weights[j:], j):
        if i != j and i != k and j != k:
          if (weight_i+weight_j+weight_k) < 200:
            counts[i] -= 1
            counts[j] -= 1
            counts[k] -= 1

sum = 0
for c, w in zip(counts, weights):
  sum += (c*w)

print(sum)