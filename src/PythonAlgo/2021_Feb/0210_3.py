# Programmers - Lv1 - Failure Rate
def solution(N, stages):
    fail = {}
    player = len(stages)
    for s in range(1, N+1):
        if player == 0:
            fail[s] = 0
        else:
            cnt = stages.count(s)
            fail[s] = cnt / player
            player -= cnt
    
    return sorted(fail, key=lambda x: fail[x], reverse=True)


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))