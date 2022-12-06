stream = input()
for i in range(len(stream)-3):
    if len(set(stream[i:i+4])) == 4:
        print(i+4)
        break