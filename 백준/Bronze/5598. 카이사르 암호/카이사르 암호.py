word = input()
before_word = ''
for i in word:
    before_word += chr((ord(i) - ord('A') + 23)%26 + ord('A'))
print(before_word)