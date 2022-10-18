n = int(input())
word_list = list(set([input() for i in range(n)]))
sort_word_list = sorted(word_list, key= lambda x: [len(x), x])

for i in sort_word_list:
    print(i)