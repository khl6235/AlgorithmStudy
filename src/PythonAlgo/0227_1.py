# Programmers - Lv2 - Quad Compress and Count
def solution(arr):
    return quad(0, 0, len(arr), arr)

def quad(x, y, l, arr):
    if l == 1:
        return [0, 1] if arr[x][y] == 1 else [1, 0]
    left_up = quad(x, y, l//2, arr)
    left_down = quad(x, y+l//2, l//2, arr)
    right_up = quad(x+l//2, y, l//2, arr)
    right_down = quad(x+l//2, y+l//2, l//2, arr)

    if left_up == left_down == right_up == right_down == [0, 1] or left_up == left_down == right_up == right_down == [1, 0]:
        return left_up
    else:
        return list(map(sum, zip(left_up, left_down, right_up, right_down)))


arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
arr2 = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
print(solution(arr))