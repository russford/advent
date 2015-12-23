class Character(object):
    def __init__(self, hp, mp):
        self.max_hp = hp
        self.max_mp = mp
        self.hp = self.max_hp
        self.mp = self.max_mp
        self.effects = []
        self.attack = 0
        self.defense = 0

    def do_effects(self, target):
        self.armor = self.defense + sum([e.armor for e in self.effects])
        for e in self.effects:
            e.act(self, target)
        self.effects = [e for e in self.effects if e.timer > 0]

class Effect(object):
    def __init__(self, name, mana_cost, timer=None, damage=0, hp_recharge=0, mp_recharge=0, armor=0):
        self.name = name
        self.timer = timer
        self.damage = damage
        self.hp_recharge = hp_recharge
        self.mp_recharge = mp_recharge
        self.armor = armor
        self.mana_cost = mana_cost

    def act(self, actor, target):
        if self.timer > 0:
            target.hp -= self.damage
            actor.hp += self.hp_recharge
            actor.mp += self.mp_recharge
            actor.mp -= self.mana_cost
            actor.armor = self.armor
        self.timer -= 1

player = Character(50, 500)
boss = Character (58,0)
boss.attack = 9

spells = [Effect("Magic Missile", 53, timer=1, damage=4),
          Effect("Drain", 73, timer= 1, damage=2, hp_recharge=2),
          Effect("Shield", 113, timer=6, armor=7),
          Effect("Poison", 173, timer=6, damage=3),
          Effect("Recharge", 229, timer=5, mp_recharge=101)]

turn = 1
while player.hp > 0 and player.mp > 0 and turn < 5:
    print ("turn %d\n------" % turn)
    print ("player hp = {.hp} mp = {.mp}".format(player))
    print ("  boss hp = {.hp} mp = {.mp}".format(boss))
    action = input("action: ")
    spell = [s for s in spells if s.name[0] == action[0]][0]
    print ("active effects:\n{}".format("\n".join([e[0] for e in player.effects])))
    player.do_effects()
    if not s in player.effects: player.effects.append(s)
    else: raise Exception ("effect already active")
    player.hp -= max(boss.attack - player.defense, 1)
    print ("after turn:")
    print ("player hp = {.hp} mp = {.mp}".format(player))
    print ("  boss hp = {.hp} mp = {.mp}".format(boss))
    turn += 1












