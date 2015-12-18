def canprocess(s,d):
    if s in d: return d[s]
    try:
        i = int(s)
    except ValueError:
        return None
    return i

def read_input (s, d, func_dict):
    action = s.split(" ")
    if len(action) == 3:
        i = canprocess(action[0],d)
        if i is not None:
            d[action[2]] = i
            return True

    elif action[0] == "NOT":
        if action[1] in d:
            d[action[3]] = ~d[action[1]]
            return True
    else:
        i = canprocess(action[0],d)
        j = canprocess(action[2],d)
        if (s[:1] == "c"):
            print ("%s, %s, %s"%(s, str(i), str(j)))
        if i is not None and j is not None:
            d[action[4]] = func_dict[action[1]](i, j)
            return True

    return False


if __name__ == "__main__":
    func_dict = { "AND": lambda x,y: x&y,
                  "OR": lambda x,y: x|y,
                  "LSHIFT": lambda x,y: x << y,
                  "RSHIFT": lambda x,y: x >> y
                }

    d = {}

    with open ("day7.txt", "r") as f:
        data = [l.strip("\n") for l in f.readlines()]

    while data:
        i=0
        while i < len(data):
            r = read_input(data[i], d, func_dict)
            if r:
                print (str(i)+"! "+data[i])
                data.pop(i)
                break
            else:
                print ("%d: not ready for %s (%d in d)" % (i, data[i], len(d)))
                i = i+1
                if i == len(data):
                    raise Exception ("hit the end")

    for k in d:
        print ("%s: %d" % (k,d[k]))

    print d["a"]
