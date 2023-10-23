import sys

input = sys.stdin.readline

n = int(input())

arr = [i for i in reversed(range(1, n + 1))]
result = [int(input()) for _ in range(n)]
temp = []
answer = ''
try:
    for number in result:

        while True:
            if len(temp) != 0 and temp[-1] == number:
                temp.pop()
                answer += "-"
                break

            temp.append(arr[-1])
            answer += "+"
            arr.pop()
except IndexError:
    print("NO")
else:
    for i in answer:
        print(i)


