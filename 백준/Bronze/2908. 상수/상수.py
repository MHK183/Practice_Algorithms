list_num = input().split()
list_new = []

for i in list_num:
    new = ''
    for j in i[-1: :-1]:
        new += j
    list_new.append(new)
print(max(list_new))