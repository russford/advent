import re

reg_int = "([+-]?\d+)"

def val(weights, data):
    score = 1
    if sum([int(data[j][5]) * weights[j] for j in range(4)]) != 500: return 0
    for i in range(4):
        score *= max(sum([int(data[j][i+1]) * weights[j] for j in range(4)]),0)
    return score

with open("day15.txt", "r") as f:
    data = [re.findall("(\w+): capacity {0}, durability {0}, flavor {0}, texture {0}, calories {0}".format(reg_int),l)[0] for l in f.readlines()]

max_weight = 0

n=100
for a1 in range(1,n-2):
    for a2 in range(a1+1,n-1):
        for a3 in range (a2+1,n):
            w = val([a1, a2-a1, a3-a2, n-a3], data)
            if w > max_weight:
                max_weight = w
                max_w = [a1, a2-a1, a3-a2, n-a3]

print (max_weight)
print (max_w)

