import copy

class KilledException(Exception):
    def __init__(self, died, cause):
        self.died = died
        self.cause = cause

class Character(object):
    def __init__(self, name, hp, mp):
        self.name = name
        self.max_hp = hp
        self.max_mp = mp
        self.hp = self.max_hp
        self.mp = self.max_mp
        self.effects = []
        self.attack = 0
        self.defense = 0
        self.mp_spent = 0

    def do_effects(self, target, g):
        self.armor = 0
        for e in self.effects:
            e.act(self, target, g)
        self.effects = [e for e in self.effects if e.timer > 0]

    def cast (self, spell, target, g):
        g.output += "{0.name} casts {1.name} for {1.mana_cost} mana\n".format(self, spell)
        self.mp -= spell.mana_cost
        if self.mp <= 0:
            raise KilledException(self, "out of mana")
        self.mp_spent += spell.mana_cost
        if spell.timer > 0:
            self.effects.append(copy.copy(spell))
        else:
            spell.timer = 1
            spell.act(self, target, g)

class Effect(object):
    def __init__(self, name, mana_cost, timer=None, damage=0, hp_recharge=0, mp_recharge=0, armor=0):
        self.name = name
        self.timer = timer
        self.damage = damage
        self.hp_recharge = hp_recharge
        self.mp_recharge = mp_recharge
        self.armor = armor
        self.mana_cost = mana_cost

    def act(self, actor, target, g):
        if self.timer > 0:
            spell_str = ', '.join(["{}={}".format(k,v) for k,v in self.__dict__.items() if type(v) is int and v>0 and k not in ["mana_cost"]])
            g.output += "{0.name} takes effect on {1.name} {2}\n".format(self, target, spell_str)
            target.hp -= self.damage
            actor.hp += self.hp_recharge
            actor.mp += self.mp_recharge
            actor.armor += self.armor
            if target.hp <= 0:
                raise KilledException(target, "out of hp")
            self.timer -= 1
            if self.timer == 0:
                g.output += "{0.name} wore off.\n".format(self)


spells = [Effect("Magic Missile", 53, timer=0, damage=4),
          Effect("Drain", 73, timer= 0, damage=2, hp_recharge=2),
          Effect("Shield", 113, timer=6, armor=7),
          Effect("Poison", 173, timer=6, damage=3),
          Effect("Recharge", 229, timer=5, mp_recharge=101)]



class Game(object):
    def __init__(self, player, boss):
        self.player = copy.copy(player)
        self.boss = copy.copy(boss)
        self.history = ""
        self.output = ""

    def take_turn (self, actor, target, action):
        self.output += "\n{0.name}'s turn\n--------\n".format(actor)
        self.output += "{0.name:<8} hp = {0.hp:<4} mp = {0.mp}\n".format(actor)
        self.output += "{0.name:<8} hp = {0.hp:<4} mp = {0.mp}\n".format(target)
        actor.do_effects(target, self)
        target.do_effects(actor, self)
        if action[0] == "A":
            dmg = max(actor.attack - (target.defense+target.armor), 1)
            self.output += "{0.name} attacks for {1} damage {2}-{3}\n".format(actor,dmg,actor.attack,(target.defense+target.armor))
            target.hp -= dmg
            if target.hp <= 0: raise KilledException(target, "out of hp")
        else:
            spell = [s for s in spells if s.name[0] == action[0]][0]
            if spell in actor.effects:
                self.output += "{0.name} already active\n".format(spell)
                raise KilledException(actor, "cast an existing spell")
            else:
                actor.cast(spell, target, self)

    def do_turn(self, action):
        self.history += action
        self.take_turn(self.player, self.boss, action)
        self.take_turn(self.boss, self.player, "A")

    def poss_actions(self):
        return [s.name[0] for s in spells if s.mana_cost < self.player.mp]


def try_game(game, min_mana):
    actions = game.poss_actions()
    min_g = None
    for a in actions:
        g = copy.deepcopy(game)
        try:
            g.do_turn(a)
            if min_mana == 0 or g.player.mp_spent < min_mana:
                min_mana = try_game (g, min_mana)
        except KilledException as e:
            if e.died.name == "boss":
                if min_mana == 0 or g.player.mp_spent < min_mana:
                    min_mana = g.player.mp_spent
                    print ("{0.history} led to death of {1.died.name}, {1.cause}, mana spent = {0.player.mp_spent}".format(g,e))
    return min_mana


player = Character("player", 50, 500)
boss = Character ("boss", 50, 0)
boss.attack = 8

g = Game(player, boss)

print (try_game(g, 0))












