# Programmers - Lv2 - Fibonacci
def solution(n):
    f1, f2 = 0, 1
    for _ in range(n):
        f1, f2 = f2, f1+f2

    return f1 % 1234567

print(solution(5))