# Programmers - Lv2 - JadenCase String
def solution(s):
    answer = ''
    arr = s.split(" ")
    for a in arr[:-1]:
        answer += a.capitalize()+" "
    answer += arr[-1].capitalize()
    return answer

s = "3people unFollowed me"
s2 = "for the last week"
print(solution(s))