fruits = int(input())
weights = [int(x) for x in input().split()]

total = sum(weights) * (2**(len(weights)-1))

def generate(weights, acc_weight, count):
  if acc_weight >= 200:
    return
  if count == 3 or len(weights) == 0:
    global total
    total -= acc_weight
    return

  generate(weights[1:], acc_weight+weights[0], count+1)
  generate(weights[1:], acc_weight, count)

generate(weights, 0, 0)

print(total)