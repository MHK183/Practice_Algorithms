while True:
    length = list(map(int, input().split()))
    # sort() 사용하기
    length.sort()
    if sum(length) == 0:
        break
    elif (length[0]**2)+(length[1]**2) == (length[2]**2):
        print('right')
    else:
        print('wrong')