passengers = []
a = 0

for _ in range(10):
    x, y = map(int, input().split())
    a += y - x
    passengers.append(a)
print(max(passengers))