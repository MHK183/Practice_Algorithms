def recursion(s, start, end, cnt):
    cnt += 1
    if start >= end:
        print(1, cnt)
    elif s[start] != s[end]:
        print(0, cnt)
    else:
        return recursion(s, start+1, end-1, cnt)

def isPalindrome(s, cnt):
    return recursion(s, 0, len(s)-1, cnt)

cnt = 0

for _ in range(int(input())):
    s = input()
    isPalindrome(s, cnt)