import sys
lines = sys.stdin.read().split("\n")

monkeys = []
count = []
current_monkey_idx = -1
for line in lines:
    if line == "":
        continue

    if line[:6] == "Monkey":
        current_monkey_idx = int(line[7:-1])
        monkeys.append({})
        count.append(0)
    elif line[:18] == "  Starting items: ":
        monkeys[current_monkey_idx]["items"] = [int(x) for x in line[17:].split(", ")]
    elif line[:19] == "  Operation: new = ":
        monkeys[current_monkey_idx]["op"] = line[19:]
    elif line[:21] == "  Test: divisible by ":
        monkeys[current_monkey_idx]["div"] = int(line[21:])
    elif line[:29] == "    If true: throw to monkey ":
        monkeys[current_monkey_idx]["true"] = int(line[29:])
    elif line[:30] == "    If false: throw to monkey ":
        monkeys[current_monkey_idx]["false"] = int(line[30:])


for _ in range(20):
    for i, monkey in enumerate(monkeys):
        for old in monkey["items"]:
            count[i] += 1
            new = eval(monkey["op"])
            new = new // 3
            if new % monkey["div"] == 0:
                monkeys[monkey["true"]]["items"].append(new)
            else:
                monkeys[monkey["false"]]["items"].append(new)
        monkey["items"] = []

count.sort(reverse=True)
print(count[0] * count[1])

