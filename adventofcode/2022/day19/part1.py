
import functools
costs = [
    [(4,0)],
    [(2,0)],
    [(3,0), (14, 1)],
    [(2,0), (7,2)]
]

costs = [
    [(2,0)],
    [(3,0)],
    [(3,0), (8, 1)],
    [(3,0), (12,2)]
]

robots = [1,0,0,0]
units = [0,0,0,0]

# ore, clay, obsidian, geode
def enough(units, costs, i):
    for u, idx in costs[i]:
        if u > units[idx]:
            return False
    return True

best = 0

@functools.cache
def rec(a,b,c,d, x,y,z,w, sec):
    if sec > 5 and b == 0:
        return 0
    if sec > 8 and c == 0:
        return 0
    if sec > 18 and d == 0:
        return 0
    # global best
    # if sec > 19 and (24 - sec) * d + w < best:
    #     # print("hola", a,b,c,d, x,y,z,w, sec)
    #     return w
    if sec == 24:
        # print(units[3])
        # if w > 0:
        #     print("adios", a,b,c,d, x,y,z,w, sec)
        return w
    robots = [a,b,c,d]
    units = [x,y,z,w]

    for i in range(4):
        units[i] += robots[i]

    
    best = max(0, rec(robots[0], robots[1], robots[2], robots[3],  units[0], units[1],units[2],units[3], sec+1))
    for i in range(4):
        if enough(units, costs, i):
            
            robots[i] += 1
            for u, idx in costs[i]:
                units[idx] -= u

            best = max(best, rec(robots[0], robots[1], robots[2], robots[3],  units[0], units[1],units[2],units[3], sec+1))

            robots[i] -= 1
            for u, idx in costs[i]:
                units[idx] += u

    
    for i in range(4):
        units[i] -= robots[i]
    return best


r = rec(robots[0], robots[1], robots[2], robots[3],  units[0], units[1],units[2],units[3], 0)

print(r)
print(rec.cache_info())
