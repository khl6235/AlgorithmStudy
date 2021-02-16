# Programmers - Lv2 - TriSnail
from itertools import chain
def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    y = -1
    x = 0
    num = 1
    # n, n-1, n-2, ... down->right->up->down...
    for i in range(n):
        for _ in range(i, n):
            if i%3 == 0:
                y += 1
            elif i%3 == 1:
                x += 1
            elif i%3 == 2:
                y -= 1
                x -= 1
            answer[y][x] = num
            num += 1
    answer = [i for i in chain(*answer) if i != 0]
    return answer

print(solution(5))