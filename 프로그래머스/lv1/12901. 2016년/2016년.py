def solution(a, b):
    weeks = ['THU','FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = sum(month[:a-1])
    day += b
    return weeks[day % 7]