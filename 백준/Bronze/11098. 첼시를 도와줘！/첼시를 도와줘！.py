for _ in range(int(input())):
    a = []
    for _ in range(int(input())):
        a.append(input().split())
    a.sort(key= lambda x:int(x[0]))
    print(a[-1][1])