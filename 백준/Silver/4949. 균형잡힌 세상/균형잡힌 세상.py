brackets = ['(', ')', '[', ']']

while True:

    string = input()

    if string == '.':
        break
    only_brackets = ''
    for letter in string:
        if letter in brackets:
            only_brackets += letter
    while '[]' in only_brackets or '()' in only_brackets:
        only_brackets = only_brackets.replace('[]', '')
        only_brackets = only_brackets.replace('()', '')
    if only_brackets:
        print('no')
    else:
        print('yes')