import re, json

def evaluate(a):
    if type(a) is int:
        return a
    if type(a) is list:
        return sum([evaluate(b) for b in a])
    if type(a) is unicode:
        try:
            return int(a)
        except:
            return 0
    if type(a) is dict:
        if "red" in a.values():
            return 0
        else:
            return sum([evaluate(v) for v in a.values()])

with open ("day12.txt", "r") as f:
    print sum([sum ([int(r) for r in re.findall("(-?\d+)", inp)]) for inp in f.readlines()])

with open ("day12.txt", "r") as f:
    l = json.load(f)
print evaluate(l)