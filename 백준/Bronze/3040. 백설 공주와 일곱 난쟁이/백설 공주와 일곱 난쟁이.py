a = [int(input()) for _ in range(9)]
b = a.copy()

for idx, i in enumerate(a[:-1]):
    for j in a[idx+1:]:
        if (i+j) == (sum(a) - 100):
            b.remove(i)
            b.remove(j)
            break
for k in b:
    print(k)
            
    