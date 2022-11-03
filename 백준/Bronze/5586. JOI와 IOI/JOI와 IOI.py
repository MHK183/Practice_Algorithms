s = input()
joi = 0
ioi = 0
i = 0
while i < len(s)-2:
    if 'JOI' == s[i:i+3]:
        joi += 1
    elif 'IOI' in s[i:i+3]:
        ioi += 1
    else:
        i += 1
        continue
    i += 2
print(joi)
print(ioi)