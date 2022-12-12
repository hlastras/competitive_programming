number = "1113222113"
for _ in range(40):
    groups = []
    current = ""
    for n in number:
        if current == "" or current[-1] == n:
            current += n
        else:
            groups.append(current)
            current = n
    groups.append(current)

    number = ""
    for g in groups:
        number += str(len(g))
        number += g[0]

print(len(number))

