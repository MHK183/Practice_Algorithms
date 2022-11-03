import sys

a = sorted([int(sys.stdin.readline().rstrip()) for _ in range(int(input()))])
for i in a:
    print(i)