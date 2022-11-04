for _ in range(int(input())):
    word, number = input().split('-')
    word_value = 0
    
    for i in range(len(word)):
        word_value += (ord(word[i]) - ord('A')) * (26**(2-i))
    
    if abs(int(number) - word_value) <= 100:
        print('nice')
    else:
        print('not nice')