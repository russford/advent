import itertools

lengths = {}

for line in open("day9.txt", "r").readlines():
    p = line.strip("\n").split(" ")
    lengths[(p[0],p[2])] = int(p[4])    

c = set([i for t in lengths.keys() for i in t])


min_l = None
max_l = None

for p in itertools.permutations(c):
    length = 0
    for i in range(len(p)-1):
        if (p[i], p[i+1]) in lengths:
            length += lengths[(p[i], p[i+1])]
        else:
            length += lengths[(p[i+1], p[i])]
    if min_l is None or length < min_l:
        min_l = length
        min_p = p
    if max_l is None or length > max_l:
        max_l = length
        max_p = p

print (str(min_p)+": %d" % min_l)
print (str(max_p)+": %d" % max_l)
        
