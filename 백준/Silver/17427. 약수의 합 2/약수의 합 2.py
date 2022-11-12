n = int(input())
answer = 0
for i in range(1, n + 1):
    answer += (n // i) * i
# 10을 예로들면
# 10이하의 정수 중 1을 약수로 두는 수는 1의 배수
# 10이하의 정수 중 2를 약수로 두는 수는 2의 배수
# 10이하의 정수 중 3을 약수로 두는 수는 3의 배수
# n이하의 정수 중 k를 약수로 두는 수는 k의 배수
print(answer)