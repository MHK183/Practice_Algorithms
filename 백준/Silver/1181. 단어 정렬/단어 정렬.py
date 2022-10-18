import sys
n = int(input())
word_list = list(set([sys.stdin.readline().strip() for i in range(n)]))
sort_word_list = sorted(word_list, key= lambda x: [len(x), x])

for i in sort_word_list:
    print(i)