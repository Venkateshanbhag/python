prod = {
    'S': [['A','B'],['C'],['b']],
    'A': [['a'], ['']],
    'B': [['b']],
    'C': [['c']]
}

for sym, prods in prod.items():
    s = set()
    for p in prods:
        s.add(p[0].lower())
        if p[0] in prod and [''] in prod[p[0]]:
            s.add('')
    print(f"FIRST({sym}) = {s}")





prod = {
    'S': [['A', 'B'], ['C', 'b']],
    'A': [['a'], ['']],
    'B': [['b']],
    'C': [['c']]
}

for sym in prod:
    s = set()
    if sym == 'S':
        s.add('$')
    for A, prods in prod.items():
        for p in prods:
            for i, X in enumerate(p):
                if X == sym:
                    if i+1 < len(p):
                        s.add(p[i+1].lower())
                    else:
                        s.add('$')
    print(f"FOLLOW({sym}) = {s}")


