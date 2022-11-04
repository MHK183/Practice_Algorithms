idx = 0
while True:
    a = input().split()
    idx += 1
    
    if a[1] == 'E':
        break
    
    a[0] = int(a[0])
    a[2] = int(a[2])
    
    if a[1] == '>':
        result = str(a[0] > a[2])
    elif a[1] == '>=':
        result = str(a[0] >= a[2])
    elif a[1] == '<':
        result = str(a[0] < a[2])
    elif a[1] == '<=':
        result = str(a[0] <= a[2])
    elif a[1] == '==':
        result = str(a[0] == a[2])
    elif a[1] == '!=':
        result = str(a[0] != a[2])
    
    print(f'Case {idx}: {result.lower()}')