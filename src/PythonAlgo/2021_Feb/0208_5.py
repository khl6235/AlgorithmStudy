# Programers - Lv1 - Sqrt
def solution(n):
    s = int(n**0.5)
    if s*s == n:
        return (s+1)**2
    else:
        return -1

n = 121
print(solution(n))