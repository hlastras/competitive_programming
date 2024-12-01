
def print_s(i, a):
    value = 0
    while a%10 == 0:
        a = a // 10
        value += 1
    print(i, value)
a = 1
for i in range(2,152):
    a *= i
    print_s(i, a)