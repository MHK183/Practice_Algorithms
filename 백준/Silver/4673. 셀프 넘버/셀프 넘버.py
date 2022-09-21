def inf_seq(n):
    n_sum = sum(list(map(int, str(n))))
    return n + n_sum

a = list(range(1, 10000 + 1))
k = []

for i in a:
    k.append(inf_seq(i))
# 중복 값 제거
k = list(set(k))

for i in k:
    if i in a:
        a.remove(i)
for i in a:
    print(i)