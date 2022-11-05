import sys
input = sys.stdin.readline
members = []
for i in range(int(input())):
    user = input().split()
    members.append((i, int(user[0]), user[1]))
members.sort(key = lambda x: (x[1], x[0]))

for member in members:
    print(member[1], member[2])