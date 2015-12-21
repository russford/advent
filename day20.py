num = 29000000

import numpy
import math
def gen_primes(upto=100):
    return filter(lambda num: (num % numpy.arange(2,1+int(math.sqrt(num)))).all(), range(2,upto+1))
import operator
import functools

def count_present_1 (n, primes, pph):
    factors = []
    prod = 1
    val = 1
    for p in primes:
        i = 0
        pi = 1
        while n % p == 0:
            i += 1
            prod *= p
            n //= p
            pi += p ** i
        val *= pi
        if prod == n:
            break
    return val * pph

def write_primes(primes):
    primes = gen_primes((num//10)+1)
    with open ("primefile.txt", "w") as f:
        f.write('\n'.join([str(p) for p in primes]))

def read_primes ():
    with open ("primefile.txt", "r") as f:
        primes = [int(l.strip('\n')) for l in f.readlines()]
    return primes

# write_primes(primes)
primes = read_primes()
print ("got {} primes".format(len(primes)))

def check_part_1 (primes):
    min_i = 0
    for i in range(665280,100, -1):
         a = count_presents(i, primes, 10)
         if a > num:
             print ("house {} gets {} presents".format(i, a))
             min_i = i

def check_part_1_2 (n):
    presents = [0]*n
    for elf in range(n):
        if elf % 1000 == 0: print (elf)
        for i in range(n):
            house_no = (elf+1)*(i+1)
            if house_no < n:
                presents[house_no-1] += 10*(elf+1)
                if presents[house_no-1] > num:
                    print ("got part 1: %d" % house_no)
                    return presents
            else:
                break


def check_part_2 (n):
    presents = [0]*n
    min_n = n
    for elf in range(n):
        for i in range(50):
            house_no = (elf+1)*(i+1)
            if house_no < n:
                presents[house_no-1] += 11 * (elf+1)
                if presents[house_no-1] > num:
                    if house_no < min_n:
                        min_n = house_no
                        print ("got it: %d" % house_no)
    return presents

# check_part_1(primes)

# check_part_1_2 (665285)

p = check_part_2 (1000000)
print (max(p), p[:10])








#
















