# Programmers - Lv1 - GCD&LCM
def solution(n, m):
    gcd = 1
    for i in range(1, min(n, m)+1):
        gcd = i if n%i == 0 and m%i == 0 and i > gcd else gcd
    lcm = n * m //gcd
    
    return [gcd, lcm]

n = 3
m = 12
print(solution(n, m))