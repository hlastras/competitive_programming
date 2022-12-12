chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def is_valid(p):
    return (any(p[i]+1 == p[i+1] and p[i+1]+1 == p[i+2] for i in range(len(p)-2))
            and all(c not in [8, 11, 14] for c in p)
            and any(p[i] == p[i+1] and p[j] == p[j+1] for i in range(len(p)-1) for j in range(i+2, len(p)-1)))

password = "hxbxxyzz"
p = [chars.index(x) for x in password]

while True:
    p[-1] += 1
    for i in range(len(p)-1, -1, -1):
        if p[i] == 26:
            p[i] = 0
            if i > 0:
                p[i-1] += 1
        else:
            break
    if is_valid(p):
        break

print(''.join([chars[x] for x in p]))