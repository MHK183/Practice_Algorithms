while True:
    sentence = input()

    if sentence == 'EOI':
        break
    # 전처리
    sentence = sentence.replace(',', ' ')
    sentence = sentence.replace('.', ' ')
    sentence = sentence.replace(')', ' ')
    sentence = sentence.replace('(', ' ')
    sentence = sentence.lower()
    
    if 'nemo' in sentence.split():
        print('Found')
    else:
        print('Missing')