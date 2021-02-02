# Programmers - Lv1 - Choose 2 & Add
def solution(numbers):
    answer = []
    for i in range(0, len(numbers)):
        for j in range(i+1, len(numbers)):
            res = numbers[i] + numbers[j]
            if res not in answer:
                answer.append(res)
    answer.sort()      
    return answer

numbers = [2,1,3,4,1]
numbers2 = [5,0,2,7]
print(solution(numbers2))