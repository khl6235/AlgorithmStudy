# Programmers - Lv1 - Descending
def solution(s):
    answer = ''.join(sorted(s, reverse=True))
    return answer

s = 'Zbcdefg'
print(solution(s))