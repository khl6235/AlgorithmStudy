# Programmers - Lv1 - Hashard
def solution(x):
    digit = 0
    q = x
    while(q > 0):
        m = q%10
        q = q//10
        digit += m
    
    return True if x%digit == 0 else False

print(solution(12))