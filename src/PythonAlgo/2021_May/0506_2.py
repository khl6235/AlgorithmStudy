# Programmers - Sorting - Largest number
def solution(numbers):
    answer = ''
    num = [str(n) for n in numbers]
    num = sorted(num, key=lambda x:x*3, reverse=True)
    if num[0] == '0':
        return '0'
    for n in num:
        answer += n
    return answer


numbers = [6, 10, 2]
numbers2 = [3, 30, 34, 5, 9]
print(solution(numbers2))