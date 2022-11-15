N = int(input())
a = sorted(map(int, input().split()))
result = 0
for i in range(len(a)):
    result += sum(a[:i + 1])
print(result)