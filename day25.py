def entry(a,b):
    return a*b + (b*b-b)//2 + (a*a-3*a+2)//2

def modulo_power(a,b,n):
    bits = len("{:b}".format(b))
    prod = 1
    for i in range(bits):
        prod = (prod*prod) % n
        if (b & (1<<(bits-i-1))):
            prod = prod * a % n
    return prod

a, b = 2947, 3029

print (20151125 * modulo_power(252533, entry(a,b)-1, 33554393) % 33554393)

