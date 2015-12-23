class HaltException(Exception):
    pass

class Computer(object):
    def __init__(self):
        self.code_ptr = 0
        self.reg = { "a":0, "b":0 }
        self.code = []

    def load(self, filename):
        with open ("day23.txt", "r") as f:
            self.code = [l.strip('\n').split(' ') for l in f.readlines()]

    def jio(self, a):
        if self.reg[a[1][0]] == 1:
            self.code_ptr += int(a[2])
        else: self.code_ptr += 1

    def jie(self, a):
        if self.reg[a[1][0]] % 2 == 0:
            self.code_ptr += int(a[2])
        else: self.code_ptr += 1

    def jmp(self, a):
        self.code_ptr += int(a[1])
        return 1

    def inc(self, a):
        self.reg[a[1][0]] += 1
        self.code_ptr += 1

    def tpl(self, a):
        self.reg[a[1][0]] *= 3
        self.code_ptr += 1

    def hlf(self, a):
        self.reg[a[1][0]] //= 2
        self.code_ptr += 1

    dispatch = { "jio": jio, "jie": jie, "jmp": jmp, "inc": inc, "tpl": tpl, "hlf": hlf }

    def execute(self):
        if self.code_ptr >= len(self.code):
            print ("at end of code")
            raise HaltException
        a = self.code[self.code_ptr]
        try:
            f = Computer.dispatch[a[0]]
        except KeyError:
            print ("unknown instruction %s" % a[0])
            raise HaltException
        f(self, a)

    def trace(self):
        if self.code_ptr < len(self.code):
            return "{:>3}: a = {:<6} b = {:<6}\t{}".format(self.code_ptr, self.reg["a"], self.reg["b"], " ".join(self.code[self.code_ptr]))

c = Computer()
c.load("day23.txt")
c.reg["a"]=1
try:
    while True:
        c.execute()
        print (c.trace())
except HaltException:
    print ("finished execution")
finally:
    print ("a = {:<6} b = {:<6}".format(c.reg["a"], c.reg["b"]))

