a, b, c = map(int , input().split())

# 3개
if a == b and b == c: 
    print(10000 + a * 1000)
# 2개
elif a == b and b != c: 
    print(1000 + a * 100)
elif b == c and c != a:
    print(1000 + b * 100)
elif c == a and a != b:
    print(1000 + c * 100)
# 1개
elif a != b and b != c:
    print(max([a, b, c]) * 100)