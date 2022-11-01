for _ in range(int(input())):
    loc, string = input().split()
    print(string[:int(loc)-1] + string[int(loc):])
    