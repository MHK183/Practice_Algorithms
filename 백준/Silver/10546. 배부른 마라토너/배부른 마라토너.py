import sys

input = sys.stdin.readline
n = int(input())
participant = [input() for _ in range(n)]
completion = [input() for _ in range(n-1)]
participant.sort()
completion.sort()
completion.append(0)
for i in range(len(participant)):
    if participant[i] != completion[i]:
        print(participant[i])
        break
    