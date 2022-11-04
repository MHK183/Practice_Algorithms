for _ in range(int(input())):
    a, b = map(int, input().split())
    s = input()
    new = ''
    for i in s:
        new += chr((a * (ord(i) - ord('A')) + b) % 26 + ord('A'))
        
    print(new)