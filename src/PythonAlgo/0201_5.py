# Programmers - Lv1 - Divide 0 Int Array
def solution(arr, divisor):
    answer = []
    for a in arr:
        if a%divisor == 0:
            answer.append(a)
    if len(answer) == 0:
        return [-1]
    return sorted(answer)

arr = [5, 9, 7, 10] #5
arr2 = [2, 36, 1, 3] #1
arr3 = [3,2,6] #10
print(solution(arr2, 1))