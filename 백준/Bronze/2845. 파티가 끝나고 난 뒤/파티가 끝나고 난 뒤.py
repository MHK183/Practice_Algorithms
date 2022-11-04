L, P = map(int, input().split())
num = L * P
news_num = list(map(int, input().split()))
for i in range(5):
    print(news_num[i] - num, end = ' ')