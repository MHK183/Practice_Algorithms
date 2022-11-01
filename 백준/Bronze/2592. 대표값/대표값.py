from collections import defaultdict
count_dict = defaultdict(int)
input_data = [int(input()) for _ in range(10)]
for i in input_data:
    count_dict[i] += 1
print(int(sum(input_data) / len(input_data)))
print(max(count_dict, key=count_dict.get))

