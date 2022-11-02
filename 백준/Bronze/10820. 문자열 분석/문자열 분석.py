while True:
    try:
        string = input()
        count = [0, 0, 0, 0]
        for i in string:
            if i.islower():
                count[0] += 1
            elif i.isupper():
                count[1] += 1
            elif i.isdigit():
                count[2] += 1
            elif i == ' ':
                count[3] += 1
        print(' '.join(map(str, count)))
    except:
        break