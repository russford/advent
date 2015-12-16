class Deer(object):
    def __init__(self, name, speed, t_burst, t_rest):
        self.name = name
        self.dist = 0
        self.speed = speed
        self.t_burst = t_burst
        self.t_rest = t_rest
        self.timer = 0
        self.score = 0

    def advance(self):
        if self.timer < self.t_burst:
            self.dist += self.speed
        self.timer += 1
        self.timer %= (self.t_burst + self.t_rest)

with open ("day14.txt", "r") as f:
    data = [l.strip('\n').split(" ") for l in f.readlines()]

deer = [Deer(d[0],  int(d[3]), int(d[6]), int(d[13])) for d in data]

for i in range(2503):
    for d in deer: d.advance()
    dist = max([d.dist for d in deer])
    for d in deer:
        if d.dist == dist:
            d.score += 1

winscore = max([d.score for d in deer])

for d in deer:
    if d.score == winscore:
        print (d.name, "wins:", d.score)



