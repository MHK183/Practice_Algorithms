a = list(map(int, input().split()))
asc = [i for i in range(1, 8 + 1)]
desc = [i for i in range(8, 0, -1)]

if a == asc:
    print("ascending")
elif a == desc:
    print("descending")
else:
    print("mixed")