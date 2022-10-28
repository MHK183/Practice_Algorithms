import sys

n = int(input())
result = 0
for i in range(n):
    a = int(sys.stdin.readline())
    result += a
print(result-(n-1))