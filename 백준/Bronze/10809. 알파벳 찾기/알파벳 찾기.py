# 단어 S 입력 (길이는 100을 넘지 않고 소문자로만 이루어짐)
s = input()
# 알파벳 소문자 리스트 만들기
alpha = list(map(chr, range(ord('a'), ord('z')+1)))
b = []
# print(ord('a'), ord('z')) 'a' 값 확인
#알파벳 처음 등장하는 위치

for i in range(len(s)):
    idx = ord(s[i]) - 97
    if type(alpha[idx]) == str:
        alpha[idx] = i
    else:
        continue

for j in range(len(alpha)):
    if type(alpha[j]) == str:
        alpha[j] = -1

for k in alpha:
    print(k, end=' ')