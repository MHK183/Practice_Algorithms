is_on = True
count = 1
while is_on:
    L, P, V = map(int, input().split())

    # 입력 끝
    is_off = (L == 0) and (P == 0) and (V == 0)
    if is_off:
        is_on = False
        continue
    day = L * (V // P)

    day += L if L < (V % P) else V % P

    print(f"Case {count}: {day}")

    count += 1
