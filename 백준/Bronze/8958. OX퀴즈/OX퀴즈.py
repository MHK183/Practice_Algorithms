test_case = int(input())

for _ in range(test_case):
    result = input()
    count = 0
    sum = 0
    for i in result:
        if i == 'O':
            count += 1
            sum += count
        else:
            count = 0
    print(sum)