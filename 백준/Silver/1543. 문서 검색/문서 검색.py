doc = input()
word = input()

new_doc = doc.replace(word, '0')
print(new_doc.count('0'))