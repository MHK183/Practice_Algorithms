# 대소문자 -> 소문자로 통일
s = input().lower()
dict_s = {}
# 딕셔너리로 사용된 알파벳 수를 저장
for i in s:
    if i in dict_s:
        dict_s[i] += 1
    else:
        dict_s[i] = 1

# 가장 많이 사용된 알파벳 찾기
max_value = 0
for key, item in dict_s.items():
    if item > max_value:
        max_value = item
        max_key = key
key_list = []
for key, item in dict_s.items():
    if item == max_value:
        key_list.append(item)

if len(key_list) == 1:
    print(max_key.upper())
else:
    print("?")