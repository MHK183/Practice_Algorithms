import sys
input = sys.stdin.readline


n = int(input())

numbers = [0] * 10001

for _ in range(n):
    numbers[int(input())] += 1

for idx in range(1, len(numbers)):
    
    for _ in range(numbers[idx]):
        print(idx)
