alpha = [chr(i) for i in range(ord('A'), ord('Z')+1)]

for _ in range(int(input())):
    s = input()
    answer = 0
    for i in alpha:
        if i not in s:
            answer += ord(i)
    print(answer)