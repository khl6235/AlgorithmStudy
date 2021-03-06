# Programmers - Lv1 - Average
def solution(arr):
    answer = 0
    for a in arr:
        answer += a
    return answer/len(arr)

arr = [1,2,3,4]
print(solution(arr))