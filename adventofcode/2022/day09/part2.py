import math
import sys
lines = sys.stdin.read().split("\n")

knots = [[0,0] for _ in range(10)]

visited = set(["0,0"])

for line in lines:
    d, n = line.split()

    for _ in range(int(n)):
        if d == "R":
            knots[0][0] += 1
        elif d == "L":
            knots[0][0] -= 1
        elif d == "U":
            knots[0][1] += 1
        elif d == "D":
            knots[0][1] -= 1

        for i in range(1, len(knots)):
            if abs(knots[i-1][0] - knots[i][0]) > 1 or abs(knots[i-1][1] - knots[i][1]) > 1:
                guess = [
                    [knots[i-1][0]-1,knots[i-1][1]], 
                    [knots[i-1][0]+1,knots[i-1][1]], 
                    [knots[i-1][0],knots[i-1][1]-1], 
                    [knots[i-1][0],knots[i-1][1]+1]
                    ]
                best_d = -1
                best_p = None

                for p in guess:
                    dist = math.sqrt((p[0] - knots[i][0])**2 + (p[1] - knots[i][1])**2)
                    if best_d == -1 or dist < best_d:
                        best_d = dist
                        best_p = p
                
                if abs(best_p[0]-knots[i][0]) >= 2 or abs(best_p[1]-knots[i][1]) >= 2:
                    guess = [
                        [knots[i-1][0]-1,knots[i-1][1]+1], 
                        [knots[i-1][0]+1,knots[i-1][1]+1], 
                        [knots[i-1][0]+1,knots[i-1][1]-1], 
                        [knots[i-1][0]-1,knots[i-1][1]-1]
                        ]
                    best_d = -1
                    best_p = None

                    for p in guess:
                        dist = math.sqrt((p[0] - knots[i][0])**2 + (p[1] - knots[i][1])**2)
                        if best_d == -1 or dist < best_d:
                            best_d = dist
                            best_p = p

                knots[i] = best_p

            else:
                break
        
        visited.add(str(knots[-1][0])+","+str(knots[-1][1]))

print(len(visited))
