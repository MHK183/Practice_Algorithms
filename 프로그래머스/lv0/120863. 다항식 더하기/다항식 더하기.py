def solution(polynomial):
    a = [i for i in polynomial.split()[0::2]]
    x = 0
    digit = 0
    for k in a:
        if 'x' in k:
            k = k.replace('x','')
            if k == '':
                x += 1
            else:
                x += int(k)
        else:
            digit += int(k)

    if x == 1:
        x = ''
    if x == 0:
        return f'{digit}'
    elif digit == 0:
        return f'{x}x'
    else:
        return f'{x}x + {digit}'