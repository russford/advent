

def is_nice_1 (s):
    print "checking "+s

    vowels = "aeiou"

    if sum([s.count(l) for l in vowels]) <3:
        return False

    for i, l in enumerate(s):
        if i < len(s)-1 and l == s[i+1]: break

    if i == len(s)-1:
        return False

    bad_str = ["ab", "cd", "pq",  "xy"]
    if any([b in s for b in bad_str]):
        return False

    return True

def is_nice_2 (s):

    for i,l in enumerate(s):
        if i < len(s)-1 and s.count(s[i:i+2])>1: break

    if i == len(s)-1:
        return False

    for i, l in enumerate(s):
        if i < len(s)-2 and l == s[i+2]: break

    if i == len(s)-1:
        return False

    return True


if __name__ == "__main__":
    with open("day5.txt", "r") as f:
        strings = f.readlines()

    print [is_nice_1(s) for s in strings].count(True)
    print [is_nice_2(s) for s in strings].count(True)

