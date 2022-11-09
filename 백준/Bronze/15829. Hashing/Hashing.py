L = int(input())
s = input()
result = 0
for i in range(len(s)):
    result += (ord(s[i])-ord('a')+1) * (31**i)
result %= 1234567891
print(result)