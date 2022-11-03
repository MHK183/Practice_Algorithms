m = int(input())
d = int(input())
s = (m-1)*31 + d
if s > 49:
    print('After')
elif s == 49:
    print('Special')
else:
    print('Before')