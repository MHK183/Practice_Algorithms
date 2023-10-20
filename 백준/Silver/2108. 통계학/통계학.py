import sys
from collections import Counter


input = sys.stdin.readline


class Calculator:
    def __init__(self, number_list):
        self.number_list = number_list

    def mean(self):
        return round(sum(self.number_list) / len(self.number_list))

    def median(self):
        sorted_number_list = sorted(self.number_list)
        return sorted_number_list[len(sorted_number_list) // 2]

    def mode(self):
        count_number_dict = Counter(self.number_list)
        max_keys = [k for k, v in count_number_dict.items() if v == max(count_number_dict.values())]
        if len(max_keys) == 1:
            return max_keys[0]
        else:
            sorted_max_keys = sorted(max_keys)
            return sorted_max_keys[1]

    def range(self):
        return max(self.number_list) - min(self.number_list)


N = int(input())

numbers = [int(input()) for _ in range(N)]

my_calculator = Calculator(numbers)
print(my_calculator.mean())
print(my_calculator.median())
print(my_calculator.mode())
print(my_calculator.range())
