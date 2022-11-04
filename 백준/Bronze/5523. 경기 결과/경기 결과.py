import sys

p1, p2 = 0, 0

for _ in range(int(input())):
    a, b = map(int, sys.stdin.readline().split())
    
    if a > b:
        p1 += 1
    elif a < b:
        p2 += 1
print(p1, p2)