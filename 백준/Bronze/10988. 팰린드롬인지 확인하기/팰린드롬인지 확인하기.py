word = input()
r_word = ''.join(list(reversed(word)))

if word == r_word:
    print(1)
else:
    print(0)