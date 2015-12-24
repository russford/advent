import itertools, functools

packs = [1, 3, 5, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]

def get_min_q (n_comp):
    target = sum(packs)//n_comp
    for i in range(3, 8):
        poss = [p for p in itertools.combinations(packs, i) if sum(p) == target]
        if len(poss) > 0: break
    else:
        return 0
    return min([functools.reduce(lambda x,y: x*y, p) for p in poss])

print (get_min_q (3))
print (get_min_q (4))

