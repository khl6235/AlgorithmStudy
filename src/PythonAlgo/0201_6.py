# Programmers - Lv1 - Ternary
def solution(n):
    answer = 0
    ter = n
    temp = ''
    while ter >= 3:
        next_ter = ter // 3
        temp += str(ter % 3)
        ter = next_ter
    
    temp += str(ter)

    for index, t in enumerate(temp):
        if t != 0:
            i = len(temp)-index-1
            answer += int(t)*(3**i)
        
    return answer

print(solution(45))