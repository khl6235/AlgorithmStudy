# Programmers - Lv1 - Hide Phone
def solution(phone_number):
    answer = ''
    for _ in range(0, len(phone_number)-4):
        answer += '*'
    answer += phone_number[-4:]
    return answer

p = "01033334444"
p2 = "027778888"
print(solution(p2))