for _ in range(int(input())):
    consume_list = []
    for _ in range(int(input())):
        s, l = input().split()
        consume_list.append((s, int(l)))
    consume_list = sorted(consume_list, key = lambda x: x[1])
    print(consume_list[-1][0])
    