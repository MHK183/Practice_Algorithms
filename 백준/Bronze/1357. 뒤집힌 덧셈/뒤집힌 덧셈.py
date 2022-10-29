def Rev(x):
    x = ''.join(reversed(x))
    return int(x)

a, b = input().split()
print(Rev(str(Rev(a)+Rev(b))))