for _ in range(int(input())):
    p1, p2 = 0, 0
    for _ in range(int(input())):
        
        a, b = input().split()
        if a == 'R':
            if b == 'S':
                p1 += 1
            elif b == 'P':
                p2 += 1
        elif a == 'P':
            if b == 'R':
                p1 += 1
            elif b == 'S':
                p2 += 1
        elif a == 'S':
            if b == 'P':
                p1 += 1
            elif b == 'R':
                p2 += 1 

        
        
    if p1 > p2:
        print('Player 1')
    elif p1 == p2: 
        print('TIE')
    else:
        print('Player 2')
