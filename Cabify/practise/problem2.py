number1, number2 = input().split()
print(max(int(number1[::-2]), int(number2[::-2])))