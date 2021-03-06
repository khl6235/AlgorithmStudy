# Programmers - Lv1 - Remove Smallest
def solution(arr):
    if len(arr) <= 1:
        return [-1]
    else:
        m = min(arr)
        arr.remove(m)
        return arr

arr = [1,3,4,2]
print(solution(arr))