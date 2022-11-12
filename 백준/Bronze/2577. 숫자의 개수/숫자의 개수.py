a = int(input())
b = int(input())
c = int(input())

abc = a * b * c
abc_s = str(abc)

for j in range(10):
    print(abc_s.count(f'{j}'))