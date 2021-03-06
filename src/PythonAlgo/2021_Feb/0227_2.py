# Programmers - Lv2 - Largest Square
import itertools
def solution(board):
    w, h = len(board), len(board[0])
    for i in range(1, w):
        for j in range(1, h):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1])+1

    return max(itertools.chain(*board))**2

board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
print(solution(board))