import math

t = int(input())

for i in range(t):
    s = int(input())
    price = 0
    for _ in range(int(input())):
        price += math.prod(map(int, input().split()))
    print(s + price)
        