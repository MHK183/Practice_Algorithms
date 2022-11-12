while True:
    try:
        n = int(input())
        for i in range(1, 100000):
            answer = int('1' * i)
            if answer % n == 0:
                print(len(str(answer)))
                break
    except:
        break