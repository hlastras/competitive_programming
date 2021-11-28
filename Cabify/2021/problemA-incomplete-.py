# def gen():
#   return "1"
input() # discard first line
degree_a = int(input())
a = [int(x) for x in input().split()]
degree_b = int(input())
b = [int(x) for x in input().split()]

r = [int() for _ in range(degree_a + degree_b + 1)]

# print(len(r))
for i, va in enumerate(a):
  print(i)
  for j, vb in enumerate(b):
    r[i+j] += va*vb
print(r)
# print("1")

# print(131071)
# r = [gen() for x in range(131070)]
# print(" ".join(r))
# print(131071)
# r = [gen() for x in range(131070)]
# print(" ".join(r))

