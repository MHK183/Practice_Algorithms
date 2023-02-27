import sys
input = sys.stdin.readline

N = int(input())
members = [input()[0] for _ in range(N)]
alpha = [chr(i) for i in range(ord('a'), ord('z') + 1)]
answer = ''


for i in alpha:
    if members.count(i) >= 5:
        answer += i
if answer == '':
    print('PREDAJA')
else:
    print(answer)