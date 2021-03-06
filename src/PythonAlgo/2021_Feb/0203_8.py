# Programmers - Lv1 - Caesar
def solution(s, n):
    answer = ''
    for i in range(0, len(s)):
        if s[i] == ' ':
            answer += ' '
            continue
        if (65 <= ord(s[i]) <= 90):
            answer += chr((ord(s[i]) - ord('A') + n)%26 + ord('A'))
        elif (97 <= ord(s[i]) <= 122):
            answer += chr((ord(s[i]) - ord('a') + n)%26 + ord('a'))

    return answer

s = "a B z"
n = 4
print(solution(s, n))