import json

def rec(object):
    if isinstance(object, dict):
        if "red" in object.values():
            return 0
        else:
            total = 0
            for k in object:
                total += rec(object[k])
            return total
    elif isinstance(object, list):
        total = 0
        for k in object:
            total += rec(k)
        return total
    elif isinstance(object, int):
        return object
    elif isinstance(object, str):
        return 0
    else:
        print("ERROR", type(object))
        return 0

print(rec(json.loads(input())))