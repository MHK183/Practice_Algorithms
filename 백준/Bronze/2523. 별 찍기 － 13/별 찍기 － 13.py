n = int(input())

for i in range(-n+1, n):
    i = abs(i)
    print('*'*(n-i))