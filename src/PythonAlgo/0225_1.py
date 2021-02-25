# Programmers - Lv2 - Carpet
def solution(brown, yellow):
    answer = []
    for i in range(1, int(yellow**0.5)+1):
        if (yellow//i)*i == yellow:
            w, h = i, yellow//i
            outline = (w+2)*2 + h*2
            if outline == brown:
                answer = [w+2, h+2]
    return sorted(answer, reverse=True)

brown, yellow = 24, 24
print(solution(brown, yellow))