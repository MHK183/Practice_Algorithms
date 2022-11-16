x = int(input())
n = 0

while True:
    n += 1
    
    if int((n**2 - n + 2) / 2) > x:
        n -= 1
        cnt = int((n**2 - n + 2) / 2)
        break


for j in range(n):
    if cnt + j == x:
        if n % 2 == 0:
            print(f'{j+1}/{n-j}')
            break
        else:
            print(f'{n-j}/{j+1}')
            break