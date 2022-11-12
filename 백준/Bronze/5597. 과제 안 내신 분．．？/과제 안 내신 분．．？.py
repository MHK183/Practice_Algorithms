n_list = [i for i in range(1, 30 + 1)]
for _ in range(28):
    n_list.remove(int(input()))
print(min(n_list))
print(max(n_list))

