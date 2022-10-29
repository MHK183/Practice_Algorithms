s = input()
answer = ''
for i in s:
    if i.isalpha():
        if i.isupper():
            answer += chr((ord(i) + 13 - ord('A')) % 26 + ord('A'))
        elif i.islower():
            answer += chr((ord(i) + 13 - ord('a')) % 26 + ord('a'))
    else:
        answer += i
print(answer)