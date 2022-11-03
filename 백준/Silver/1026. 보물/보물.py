n = int(input())
a = sorted(list(map(int, input().split())))
b = list(map(int, input().split()))
answer = 0
# max값을 곱하고 제거해주기 (b 정렬하면 안되는 조건 지키기)
for i in range(n):
    answer += a[i] * max(b)
    b.remove(max(b))
print(answer)