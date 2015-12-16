import itertools

happy = {}

for line in open("day12.txt", "r").readlines():
    p = line.strip(".\n").split(" ")
    happy[(p[0],p[10])] = int(p[3]) * (-1 if p[2] == "lose" else 1)

c = set([i for t in happy.keys() for i in t])

for person in c:
    happy[("Russ", person)] = 0
    happy[(person, "Russ")] = 0

c.add("Russ")

max_l = None

def get_h (i,j,happy):
    if (i,j) in happy:
        return happy[(i,j)]
    else:
        return happy[(j,i)]

l = len(c)
for p in itertools.permutations(c):
    h = 0
    for i in range(len(p)):
        h += happy [(p[i], p[(i-1)%l])]
        h += happy [(p[i], p[(i+1)%l])]
    if max_l is None or h > max_l:
        max_l = h
        max_p = p

print (str(max_p)+": %d" % max_l)

