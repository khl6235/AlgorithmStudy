# Programmers - Lv1 - Descending Int
def solution(n):
    temp = []
    q = n
    while(q > 0):
        m = q%10
        q = q//10
        temp.append(m)
    temp = sorted(temp, reverse=True)
    ans = ''
    for i in temp:
        ans += str(i)
    
    return int(ans)

n = 118372
print(solution(n))