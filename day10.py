import itertools, time

def iterate(s):
    s1 = ""
    ci = s[0]
    i=0
    for c in s:
        if ci == c: i += 1
        else:
            s1 += "%d%s" % (i,ci)
            i=1
            ci=c
    s1 += "%d%s" % (i,ci)
    return s1

def iterate2(s):
    return ''.join([str(len(list(v)))+str(k) for k,v in itertools.groupby(s)])

s = "1321131112"

start = time.time()
for i in range(50):
    s = iterate2(s)
print ("%.02fs" % (time.time()-start))

print (len(s))
        
