import itertools

number = "1113222113"
for _ in range(50):
    groups = [list(group) for _, group in itertools.groupby(number)]

    number = ""
    for g in groups:
        number += str(len(g))
        number += g[0]

print(len(number))

