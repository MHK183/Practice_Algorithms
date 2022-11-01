for _ in range(int(input())):
    p, m = map(int, input().split())
    arrive = [int(input()) for _ in range(p)]
    print(len(arrive) - len(set(arrive)))