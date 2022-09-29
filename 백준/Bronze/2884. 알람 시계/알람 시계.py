num = list(map(int, input().split()))
if num[1] >= 45:
    print(num[0], num[1] - 45)
elif num[0] >= 1:
    print(num[0] - 1, (60 + num[1]) - 45)
elif num[0] < 1:
    print(23, (60 + num[1]) - 45)
