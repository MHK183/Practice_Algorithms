for _ in range(int(input())):
    answer = []
    for i in input():
        answer.append(i)
        if answer[-2:] == ['(',')']:
            for _ in range(2):
                answer.pop()

    if len(answer) == 0:
        print('YES')
    else:
        print('NO')