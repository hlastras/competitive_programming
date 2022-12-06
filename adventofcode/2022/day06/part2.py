stream = input()
for i in range(len(stream)-13):
    if len(set(stream[i:i+14])) == 14:
        print(i+14)
        break