import sys

numbers = []
for _ in range(int(input())):
    number = int(sys.stdin.readline())
    if number == 0:
        numbers.pop()
    else:
        numbers.append(number)
print(sum(numbers))