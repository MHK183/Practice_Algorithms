L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

korean = A / C
math = B / D

if korean > A // C:
    korean = int(korean) + 1
else:
    korean = int(korean)
if math > B // D:
    math = int(math) + 1
else:
    math = int(math)
print(L - max(korean, math))