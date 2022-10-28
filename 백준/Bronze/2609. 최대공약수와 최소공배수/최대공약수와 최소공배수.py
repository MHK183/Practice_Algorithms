a, b = map(int, input().split())
x, y = a, b
while b != 0:
    r = a % b
    a, b = b, r
print(a)
print(x*y//a)