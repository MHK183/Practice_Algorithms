import sys
from collections import Counter
# input = sys.stdin.readline

N = int(input())
number_cards = Counter(input().split())
M = int(input())
have_counts = input().split()

answer = []

for num in have_counts:
    answer.append(str(number_cards[num]))

print(' '.join(answer))