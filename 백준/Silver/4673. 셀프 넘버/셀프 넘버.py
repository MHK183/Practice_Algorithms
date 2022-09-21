def inf_seq(n):
    n_sum = sum(list(map(int, str(n))))
    result = n + n_sum
    if result <= 10000:
        return result

a = list(range(1, 10000 + 1))

k = []
for i in a:
    k.append(inf_seq(i))

k = set(k)
k = list(k)


for i in k:
    if i in a:
        a.remove(i)
for i in a:
    print(i)