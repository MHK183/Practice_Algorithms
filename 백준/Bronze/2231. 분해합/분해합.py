n = int(input())

for i in range(1, n+1):
    s = str(i)
    k = i
    for j in s:
        k += int(j)
    if n == k:
        print(i)
        break
if n != k:
    print(0)