# Programmers - Lv2 - Largest Number
def solution(numbers):
    num = [str(numbers[i]) for i in range(len(numbers))]
    num.sort(key= lambda x:x*3, reverse=True)
    if num[0] == '0':
        return '0'
    return ''.join(num)

numbers = [6, 10, 2]
numbers2 = [3, 30, 34, 5, 9]
numbers3 = [0, 0, 0, 0]
print(solution(numbers3))