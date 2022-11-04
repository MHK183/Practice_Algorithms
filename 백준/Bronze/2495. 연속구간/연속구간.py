for _ in range(3):
    a = []
    s = input() + 'k'
    i = 0
    while i < len(s):

        cnt = 1
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                cnt += 1
            else:
                a.append(cnt)
                break
        i += cnt
    print(max(a))