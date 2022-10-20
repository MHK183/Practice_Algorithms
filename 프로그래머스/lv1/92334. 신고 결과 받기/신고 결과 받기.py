def solution(id_list, report, k):
    answer = []
    user_dict = {user_id : [] for user_id in id_list}
    report_user = {}
    ban_list = []
    # 신고한 유저의 신고목록
    for i in report:
        n = i.split()
        user_dict[n[0]].append(n[1])
        user_dict[n[0]] = list(set(user_dict[n[0]]))
    # 신고당한 유저 횟수 세기
    for i in user_dict:
        for j in user_dict[i]:
            if j not in report_user:
                report_user[j] = 1
            else:
                report_user[j] += 1
    # 신고당한 유저로 정지 목록 만들기
    for key in report_user:
        if report_user[key] >= k:
            ban_list.append(key)
    # 정지먹은 유저를 신고한 유저에게 메일 보내기
    for _, user_id in user_dict.items():
        mail_cnt = 0
        for u in user_id:
            if u in ban_list:
                mail_cnt += 1
        answer.append(mail_cnt)
    return answer