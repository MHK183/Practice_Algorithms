import sys
rsp = {'R':'S', 'S':'P', 'P':'R'}

for _ in range(int(input())):
    p1, p2 = 0, 0
    for _ in range(int(input())):
        
        a, b = sys.stdin.readline().split()
        if rsp[a] == b:
            p1 += 1
        elif a == b:
            continue
        else:
            p2 += 1
        
        
    if p1 > p2:
        print('Player 1')
    elif p1 == p2: 
        print('TIE')
    else:
        print('Player 2')
