input()
a = map(str, sorted(list(map(int, set(input().split())))))
print(' '.join(a))
