a = [int(input()) for _ in range(9)]
b = a.copy()
l = len(a)

for i in range(l-1):
    for j in range(i+1, l):
        if (a[i]+a[j]) == (sum(a) - 100):
            b.remove(a[i])
            b.remove(a[j])
            break
for k in b:
    print(k)