# Programmers - Lv1 - 2016
def solution(a, b):
    answer = ''
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    temp = 0
    for m in range(0, a-1):
        temp += months[m]

    temp += b
    answer = days[(temp+3)%7]
    return answer

print(solution(5, 24))