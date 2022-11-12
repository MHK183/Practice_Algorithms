import sys
t = int(sys.stdin.readline().rstrip())
# t = int(input())

for i in range(t):
    output = ''
    for _ in range(i+1):
        output += '*'
    print(output)