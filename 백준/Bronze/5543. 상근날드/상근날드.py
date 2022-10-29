price = [int(input()) for _ in range(5)]
print(min(price[:3]) + min(price[3:]) - 50)
    