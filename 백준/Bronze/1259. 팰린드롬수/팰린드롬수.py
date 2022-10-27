while True:
    word = list(input())
    new_word = word.copy()
    new_word.reverse()
    if word[0] == '0':
        break
    elif word == new_word:
        print('yes')
    else:
        print('no')