def solution(dots):
    # 기울기가 같은 경우가 평행이다
    # A, B, C, D
    # A, B : C, D // A, C : B, D // A, D : B, C
    # 위를 보면 A랑 맞는 짝만 찾아도 경우의 수가 전부 나옴

    for dot in dots[1:]:
        dots_b = dots[1:].copy()
        dots_a = [dots[0]]
        # 두 점을 짝지음
        dots_a.append(dot)
        dots_b.remove(dot)
        # 두 점의 기울기를 구해서 비교 (x 증가량이 0인 경우에는 1로 설정)
        if (dots_a[0][0] - dots_a[1][0]) == 0:
            gradient_a = 1
        else:
            gradient_a = (dots_a[0][1] - dots_a[1][1]) / (dots_a[0][0] - dots_a[1][0])
        if (dots_b[0][0] - dots_b[1][0]) == 0:
            gradient_b = 1
        else:
            gradient_b = (dots_b[0][1] - dots_b[1][1]) / (dots_b[0][0] - dots_b[1][0])


        if gradient_a == gradient_b:
            return 1


    return 0
  