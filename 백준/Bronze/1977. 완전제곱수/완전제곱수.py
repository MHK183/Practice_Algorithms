m = int(input())
n = int(input())

psn_list = []
for i in range(m, n+1):
    if i ** (1/2) == int(i ** (1/2)):
        psn_list.append(i)
if len(psn_list) == 0:
    print(-1)
else:
    print(sum(psn_list))
    print(min(psn_list))