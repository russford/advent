def init_matrix (n):
    m = [[0] * n for i in range(n)]
    return m

def process_action (m, a, act_dict):
    acts = act_dict.keys()
    for ai in acts:
        if a[:len(ai)] == ai:
            break
        
    f = act_dict[ai]
    
    data = a[len(ai)+1:].split(" ")
    x1, y1 = [int(i) for i in data[0].split(",")]
    x2, y2 = [int(i) for i in data[2].split(",")]
    
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            m[i][j] = f(m[i][j])

def do_grid (act_dict, actions):
    m = init_matrix (1000)
    for a in actions:
        process_action(m, a, act_dict)
    return (sum([sum(r) for r in m]))
    

if __name__ == "__main__":
    m = init_matrix(1000)

    with open("day6.txt", "r") as f:
        actions = f.readlines()

    act_dict1 = { "turn off": (lambda a: 0),
                  "turn on": (lambda a: 1),
                  "toggle": (lambda a: (1-a)) }
    
    act_dict2 = { "turn off": (lambda a: a-1 if a>0 else 0),
                  "turn on": (lambda a: a+1),
                  "toggle": (lambda a: a+2) }

        
    print (do_grid(act_dict1, actions))
    print (do_grid(act_dict2, actions))
    

    
