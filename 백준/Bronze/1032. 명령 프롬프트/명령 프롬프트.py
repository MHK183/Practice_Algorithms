files = [input() for _ in range(int(input()))]
answer = list(files[0])

for file in files[1:]:
    for i in range(len(answer)):
        if answer[i] == file[i]:
            answer[i] = file[i]
        else:
            answer[i] = '?'
print(''.join(answer))