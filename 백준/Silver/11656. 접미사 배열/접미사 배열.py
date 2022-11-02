s = input()
suffix = sorted([s[i:] for i in range(len(s))])
for i in suffix:
    print(i)
