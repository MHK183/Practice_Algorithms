word = input()
new_word = ''
for char in word:
    if char.isupper():
        new_word += char.lower()
    elif char.islower():
        new_word += char.upper()
print(new_word)