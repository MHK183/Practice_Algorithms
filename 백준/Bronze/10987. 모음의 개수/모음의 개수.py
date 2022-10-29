s = input()
mo = ['a', 'e', 'i', 'o', 'u']
cnt = 0

for i in mo:
    cnt += s.count(i)
    
print(cnt)