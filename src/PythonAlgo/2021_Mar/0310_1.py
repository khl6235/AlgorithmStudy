# Programmers - Lv2 - Max & Min
def solution(s):
    answer = ''
    arr = list(map(int, s.split(' ')))
    answer += str(min(arr))+" "
    answer += str(max(arr))
    return answer

s = "1 2 3 4"
s2 = "-1 -2 -3 -4"
print(solution(s2))