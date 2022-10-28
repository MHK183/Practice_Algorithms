remain_apple = 0
for i in range(int(input())):
    student, apple = map(int, input().split())
    remain_apple += apple % student
print(remain_apple)