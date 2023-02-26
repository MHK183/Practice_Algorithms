answer = ''
alpha_dict = {}

while True:
    try:
        sentence = input()
        sentence = sentence.replace(' ', '')
        for i in sentence:
            if i not in alpha_dict:
                alpha_dict[i] = 1
            else:
                alpha_dict[i] += 1
    except EOFError:
        break

for key, value in alpha_dict.items():
    if value == max(alpha_dict.values()):
        answer += key
answer = ''.join(sorted(answer))
print(answer)