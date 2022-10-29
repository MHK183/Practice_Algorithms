a = [int(input()) for _ in range(9)]
l = len(a)

for i in range(l-1):
    for j in range(i+1, l):
        if (a[i]+a[j]) == (sum(a) - 100):
            a.remove(a[i])
            a.remove(a[j-1])
            break
    if sum(a) == 100:
        break
for k in a:
    print(k)