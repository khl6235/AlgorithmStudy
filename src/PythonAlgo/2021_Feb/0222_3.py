# Programmers - Lv2 - Target Number
def solution(numbers, target):
    result = [0]
    for i in numbers:
        sub = []
        for j in result:
            sub.append(j+i)
            sub.append(j-i)
        result = sub
    return result.count(target)

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))