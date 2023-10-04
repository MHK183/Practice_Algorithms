s = input() + 'x'
zero_count = 0
one_count = 0

previous_char = s[0]

for current_char in s[1:]:
    if current_char != previous_char:
        if previous_char == '0':
            zero_count += 1
        elif previous_char == '1':
            one_count += 1

        previous_char = current_char

print(min(zero_count, one_count))