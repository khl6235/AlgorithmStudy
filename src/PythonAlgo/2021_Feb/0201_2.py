# Programmers - Lv1 - SeoulKim

def solution(seoul):
    answer = '김서방은 '
    answer += str(seoul.index('Kim'))+'에 있다'
    return answer

seoul = ["Jane", "Kim"]
print(solution(seoul))