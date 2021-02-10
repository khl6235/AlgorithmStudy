# Programmers - Lv1 - Secret Map
def solution(n, arr1, arr2):
    answer = []
    for i in range(0, n):
        b = bin(arr1[i] | arr2[i])[2:]
        b = b.zfill(n)
        tmp = ''
        for j in range(0, n):
            tmp += '#' if b[j] == '1' else ' '

        answer.append(tmp)

    return answer

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
n2 = 6
arr12 = [46, 33, 33 ,22, 31, 50]
arr22 = [27 ,56, 19, 14, 14, 10]
print(solution(n2, arr12, arr22))