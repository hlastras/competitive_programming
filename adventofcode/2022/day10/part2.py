import sys
lines = sys.stdin.read().split("\n")

x = 1
read_line = True
next_value = 0
for _ in range(6):
    crt = []
    for i in range(40):
        if read_line:
            x += next_value
            next_value = 0
            line = lines[0]
            lines = lines[1:]

            if line != "noop":
                _, value = line.split()
                next_value = int(value)
                read_line = False
        else:
            read_line = True

        if i == x-1 or i == x or i == x+1:
            crt.append("#")
        else:
            crt.append(".")
    print("".join(crt))



