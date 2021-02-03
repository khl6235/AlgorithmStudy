# Programmers - Lv1 - Mid Letter
def solution(s):
    mid = len(s)//2
    if len(s)%2 != 0:
        answer = s[mid]
    else:
        answer = s[mid-1:mid+1]

    return answer

s = "abcde"
print(solution(s))