for _ in range(int(input())):
    num = ''.join(bin(int(input()))[2:][::-1])
    
    for i in range(len(num)):
        if num[i] == '1':
            print(i, end=' ')