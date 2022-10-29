for _ in range(int(input())):
    elements = list(map(int, input().split()))
    elements.sort(reverse=True)
    print(elements[3 - 1])