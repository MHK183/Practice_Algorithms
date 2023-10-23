import sys

input = sys.stdin.readline


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
K = int(input())

locations = [list(map(lambda x: int(x)-1, input().split())) for _ in range(K)]

for loc in locations:
    sum_arr = 0
    for i in range(loc[0], loc[2] + 1): # x
        for j in range(loc[1], loc[3] + 1): # y
            sum_arr += arr[i][j]
    print(sum_arr)