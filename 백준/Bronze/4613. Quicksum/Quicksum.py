alpha = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

while True:
    
    s = input()
    
    if s == '#':
        break
    
    quicksum = 0
    
    for i in range(len(s)):
        if s[i] == ' ':
            continue
        quicksum += (i+1) * (alpha.index(s[i])+1)
    
    print(quicksum)