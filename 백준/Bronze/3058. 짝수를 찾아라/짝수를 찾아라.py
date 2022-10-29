for _ in range(int(input())):
    arr = []
    t = list(map(int, input().split()))
    for i in t:
        if i % 2 == 0:
            arr.append(i)
    print(sum(arr), min(arr))