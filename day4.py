from hashlib import md5

def find_hash_key (t,n):
    m = md5(t)
    for i in range(10000000):
        m2 = m.copy()
        m2.update(str(i))
        if m2.hexdigest()[:n] == '0'*n:
            return i

print (find_hash_key('ckczppom',5))
print (find_hash_key('ckczppom',6))