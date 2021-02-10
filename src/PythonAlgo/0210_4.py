# Programmers - Lv1 - Dart Game
def solution(dartResult):
    score = []
    num = ''
    for i in dartResult:
        if i.isnumeric():
            num += i
        elif i in ['S', 'D', 'T']:
            fac = {'S':1, 'D':2, 'T':3}[i]
            score.append(int(num) ** fac)
            num = ''
        elif i == '*':
            score[-1] *= 2
            if len(score) > 1:
                score[-2] *= 2
        elif i == '#':
            score[-1] *= -1
    
    return sum(score)

dartResult = "1S2D*3T"
dartResult2 = "1D2S#10S"
print(solution(dartResult2))