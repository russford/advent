from collections import defaultdict

cont_list = [43,3,4,10,21,44,4,6,47,41,34,17,17,44,36,31,46,9,27,38]

n = len(cont_list)
cont = defaultdict(int)

for i in range(1 << n):
    c = 0
    vol = 0
    for j in range(n):
        if i&(1<<j):
            vol += cont_list[j]
            c += 1
    if vol == 150:
        cont[c] += 1

print (sum(cont.values()))
print(cont[min(cont.keys())])

