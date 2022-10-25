while True:
    n = int(input())
    if n == -1:
        break
    answer = 0
    output = f'{n} = '
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            answer += i
            output += f'{str(i)} + '
    if n == answer:
        print(output[:-3])
    else:
        print(f'{n} is NOT perfect.')
        