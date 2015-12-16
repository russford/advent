if __name__ == "__main__":
    with open("c:/code/python/advent/day8.txt", "r") as f:
        s = [l.strip("\n") for l in f.readlines()]

    print (sum([len(a) - len(eval(a)) for a in s]))
    print (sum([a.count("\"")+a.count("\\")+2 for a in s] ))
