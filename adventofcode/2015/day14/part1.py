import sys
lines = sys.stdin.read().split("\n")

best = 0
time = 2503
for line in lines:
    data = line.split()
    speed = int(data[3])
    fly = int(data[6])
    rest = int(data[13])

    distance = (time // (fly+rest)) * (fly * speed) + min(fly, time % (fly+rest)) * speed
    best = max(best, distance)
print(best)