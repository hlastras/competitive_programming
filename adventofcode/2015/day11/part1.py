chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def is_valid(p):
    valid = False
    for i in range(0, len(p)-2):
        if p[i]+1 == p[i+1] and p[i+1]+1 == p[i+2]:
            valid = True
            break
    if not valid:
        return False

    for c in p:
        if c == 8 or c == 11 or c == 14:
            return False

    for i in range(len(p)-1):
        for j in range(i+2, len(p)-1):
            if p[i] == p[i+1] and p[j] == p[j+1]:
                return True

    return False

password = "hxbxwxba"
p = [chars.index(x) for x in password]
while True:
    # iterate
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