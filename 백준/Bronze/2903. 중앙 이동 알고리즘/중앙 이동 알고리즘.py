N = int(input())

answer = 2
for i in range(N):
    answer += 2**i

print(answer ** 2)