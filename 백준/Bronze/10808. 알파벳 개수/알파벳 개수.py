s = input()

alpha = [chr(ord('a')+i) for i in range(26)]
for i in alpha:
    print(s.count(i), end=' ')