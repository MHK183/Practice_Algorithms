n = int(input())
count = 0

for _ in range(n):
    break_word = True
    word = input()

    for idx, i in enumerate(word):
        alpha = i
        for j in range(idx+1, len(word)):
            if word.rfind(alpha) > word.rfind(word[j]):
                break_word = False
                break
        if not break_word:
            break

    if break_word:
        count += 1
print(count)