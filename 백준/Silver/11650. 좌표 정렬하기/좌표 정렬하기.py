n = int(input())
num_list = []
for _ in range(n):
    num_list.append(list(map(int, input().split())))

num_list = sorted(num_list, key = lambda x: [x[0], x[1]])
    
for idx, _ in enumerate(num_list):
    print(num_list[idx][0], num_list[idx][1])