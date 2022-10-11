while True:
    length = list(map(int, input().split()))
    bit = max(length) # 빗변
    length_1 = length.copy()
    length_1.remove(bit)
    if sum(length) == 0:
        break
    elif (length_1[0]**2)+(length_1[1]**2) == (bit**2):
        print('right')
    else:
        print('wrong')