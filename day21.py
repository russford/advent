weapons = [["Dagger",       8,     4,       0],
           ["Shortsword",   10,     5,       0],
           ["Warhammer",    25,    6,       0],
           ["Longsword",    40,     7,       0],
           ["Greataxe",    74,     8,       0]]

armor = [["None", 0, 0, 0],
         ["Leather",      13,     0,       1],
         ["Chainmail",    31,     0,       2],
         ["Splintmail",   53,     0,       3],
         ["Bandedmail",   75,     0,       4],
         ["Platemail",   102,     0,       5]]

rings = [["None", 0, 0, 0],
         ["None", 0, 0, 0],
         ["Damage +1",    25,     1,       0],
         ["Damage +2",    50,     2,       0],
         ["Damage +3",   100,     3,       0],
         ["Defense +1",   20,     0,       1],
         ["Defense +2",   40,     0,       2],
         ["Defense +3",   80,     0,       3]]


b_hp = 109
b_att = 8
b_def = 2

p_hp = 100

def player_wins (p_att, p_def):
    p_dmg = max(p_att - b_def, 1)
    b_dmg = max(b_att - p_def, 1)
    p_turns = (b_hp // p_dmg) + 1
    b_turns = (p_hp // b_dmg) + 1
    return p_turns <= b_turns

def equip (items):
    return [sum([item[i+1] for item in items]) for i in range(3)]


min_cost = 100000
max_cost = 0
for i in range(len(weapons)):
    for j in range(len(armor)):
        for k in range(len(rings)):
            for l in range(k+1,len(rings)):
                equipment = [weapons[i], armor[j], rings[k], rings[l]]
                cost, a, d = equip(equipment)
                if player_wins (a,d):
                    if cost < min_cost:
                        min_cost = cost
                        min_equip = equipment
                else:
                    if cost > max_cost:
                        max_cost = cost
                        max_equip = equipment

print ("min set to win : {} gold, {}".format(min_cost, str(min_equip)))
print ("max set to lose: {} gold, {}".format(max_cost, str(max_equip)))



