while True:
    try:
        n = int(input())
        i = 0
        answer = 0
        while True:
            i += 1
            answer = answer * 10 + 1
            answer %= n
            if answer == 0:
                print(i)
                break
    except:
        break