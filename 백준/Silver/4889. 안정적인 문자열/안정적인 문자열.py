loop_count = 0


def count_operate(letters):
    count = 0
    while '{}' in letters:
        letters = letters.replace('{}','')

    for i in range(0, len(letters), 2):
        if letters[i:i+2] == '}}' or letters[i:i+2] == '{{':
            count += 1
        elif letters[i:i+2] == '}{':
            count += 2

    return count


while True:
    input_letters = input()

    if '-' in input_letters:
        break

    answer = count_operate(input_letters)
    loop_count += 1

    print(f"{loop_count}. {answer}")
