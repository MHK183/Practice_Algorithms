def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


N = int(input())
number = str(factorial(N))
answer = 0

for count, i in enumerate(reversed(number)):
    if i != '0':
        answer = count
        break
print(answer)