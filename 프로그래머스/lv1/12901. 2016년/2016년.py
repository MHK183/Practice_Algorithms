def solution(a, b):
    weeks = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED','THU']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = sum(month[:a-1])
    day += b - 1 
    return weeks[day % 7]