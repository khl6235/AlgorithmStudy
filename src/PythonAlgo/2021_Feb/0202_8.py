# Programmers - Lv1 - Crane Game
def solution(board, moves):
    answer = 0
    bucket = []
    for m in moves:
        for b in board:
            if b[m-1] != 0:
                bucket.append(b[m-1])
                b[m-1] = 0
                break
        if len(bucket) > 1 and bucket[-1] == bucket[-2]:
            bucket = bucket[:-2]
            answer += 2

    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))