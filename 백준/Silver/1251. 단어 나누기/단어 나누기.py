# 임의의 두 부분을 자름 (길이는 최소 1이상)
# 세 개의 작은 단어들을 앞뒤로 뒤집기
# 다시 합쳤을 때 사전 순으로 가장 빨라야함
# ord를 안써도 기본적으로 아스키코드 값이 내장 되어 있음
# 자르는 방법을 생각할 필요없이 모든 경우의 수를 리스트에 저장 후
# sort() 로 사전순으로 정렬

word = input()
words = []
l = len(word)

for i in range(l-2):
    for j in range(i+1, l-1):
        for k in range(j+1, l):
            first, second, third = word[:j], word[j:k], word[k:]
            words.append(first[::-1] + second[::-1] + third[::-1])
words.sort()
print(words[0])