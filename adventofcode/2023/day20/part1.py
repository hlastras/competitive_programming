import sys
lines = sys.stdin.read().split("\n")



def parse_workflow(line):
    idx = line.find("{")
    name = line[:idx]
    raw_rules = line[idx+1:-1].split(",")
    rules = []
    for raw_rule in raw_rules:
        idx1 = max(raw_rule.find(">"), raw_rule.find("<"))
        idx2 = raw_rule.find(":")
        if idx1 == -1 or idx2 == -1:
            rules.append((raw_rule, None, None, None))
            continue
        go_to = raw_rule[idx2+1:]
        property = raw_rule[:idx1]
        value = int(raw_rule[idx1+1:idx2])
        operation = raw_rule[idx1:idx1+1]
        rules.append((go_to, property, value, operation))
    return name, rules

def parse_piece(line):
    result = {}
    items = line[1:-1].split(",")
    for item in items:
        idx = item.find("=")
        result[item[:idx]] = int(item[idx+1:])
    return result


wf = {}
wf["A"] = "Accepted"
wf["R"] = "Rejected"
phase = 1
total = 0
for line in lines:
    if line == "":
        phase = 2
        continue

    if phase == 1:
        name, rules = parse_workflow(line)
        wf[name] = rules
    if phase == 2:
        piece = parse_piece(line)
        cwf = wf["in"]
        while True:
            if cwf == "Accepted":
                print("Accepted")
                total += sum(piece.values())
                break
            if cwf == "Rejected":
                print("Rejected")
                break

            for rule in cwf:
                go_to, property, value, operation = rule

                if property is None:
                    cwf = wf[go_to]
                    break
                if operation == ">" and piece[property] > value:
                    cwf = wf[go_to]
                    break
                if operation == "<" and piece[property] < value:
                    cwf = wf[go_to]
                    break
print(total)
        


