def wrap_len(a,b,c):
    return 2*a*b + 2*a*c + 2*b*c + a*b*c/max(a,b,c)

def ribbon_len(a,b,c):
    return 2*(a+b+c-max(a,b,c))+a*b*c

if __name__ == "__main__":
    inp = open ("day2.txt", "r").readlines()
    inp = [[int(b) for b in a.strip("\n").split("x")] for a in inp]
    print (sum([wrap_len(a[0],a[1],a[2]) for a in inp]))
    print (sum([ribbon_len(a[0],a[1],a[2]) for a in inp]))
