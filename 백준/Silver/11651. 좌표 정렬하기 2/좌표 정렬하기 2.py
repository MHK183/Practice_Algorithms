import sys

coordinate = []

for _ in range(int(input())):
    coordinate.append(list(map(int, sys.stdin.readline().split())))
coordinate.sort(key = lambda x : (x[1], x[0]))

for i in coordinate:
    print(i[0], i[1])