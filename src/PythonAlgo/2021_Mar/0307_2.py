# Programmers - Lv2 - Visit Length
d = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}

def solution(dirs):
    # 경로에 중복이 없어야 하므로 set
    visited = set()
    x, y = 0, 0
    for i in dirs:
        dx, dy = d[i]
        nx, ny = x+dx, y+dy
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            # 가능한 범위 내에서 정방향과 역방향 좌표 셋을 두가지 만들어두고, 다음 포인트로 옮겨감
            path = (x, y, nx, ny)
            path_re = (nx, ny, x, y)
            x, y = nx, ny

            # 이미 지나간 길이 아니라면 visited에 정방향, 역방향 좌표 셋을 집어넣어둔다
            if path not in visited:
                visited.add(path)
                visited.add(path_re)

    # 양방향 다 집어넣어두었기 때문에 반 나눈 값을 리턴
    return len(visited)//2

dirs = "ULURRDLLU"
print(solution(dirs))