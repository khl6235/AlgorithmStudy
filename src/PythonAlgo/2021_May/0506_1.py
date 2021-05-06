# Programmers - Sorting - Kth number
def solution(array, commands):
    answer = []
    for c in commands:
        tmp = array[c[0]-1:c[1]]
        tmp.sort()
        answer.append(tmp[c[2]-1])

    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))