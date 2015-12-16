import re

data = {}

with open("day16.txt", "r") as f:
    for l in f.readlines():
        d = {}
        s = re.findall("Sue (\d+):", l)[0]
        for a in re.findall("(\w+: \d+,*)+", l):
            k,v = a.strip(",").split(": ")
            d[k] = int(v)
        data[s] = d

print(data)

match = { "children": 3,
          "cats": 7,
          "samoyeds": 2,
          "pomeranians": 3,
          "akitas": 0,
          "vizslas": 0,
          "goldfish": 5,
          "trees": 3,
          "cars": 2,
          "perfumes": 1 }

print (data['103'])

for s,d in data.items():
    for k,v in d.items():
        if k in ["trees", "cats"]:
            if v <= match[k]:
                break
        elif k in ["pomeranians", "goldfish"]:
            if v >= match[k]:
                break
        elif v != match[k]:
            break
    else:
        print (s, d)