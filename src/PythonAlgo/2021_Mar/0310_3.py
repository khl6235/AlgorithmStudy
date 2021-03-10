# Programmers - Lv2 - Matrix Multiplication
def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        arr = []
        for k in range(len(arr2[0])):
            tmp = 0
            for j in range(len(arr2)):
                tmp  += arr1[i][j]*arr2[j][k]
            arr.append(tmp)
        answer.append(arr)
    return answer

arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]
arr11 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr22 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
print(solution(arr11, arr22))
