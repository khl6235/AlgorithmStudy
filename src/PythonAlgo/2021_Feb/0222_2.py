# Programmers - Lv2 - Life Boat
def solution(people, limit):
    answer = 0
    people.sort()
    a = 0
    b = len(people)-1
    while a <= b:
        answer += 1
        if people[a] + people[b] <= limit:
            a += 1
        b -= 1

    return answer

people = [70, 50, 80, 50]
limit = 100
people2 = [70, 80, 50]
limit2 = 100
print(solution(people, limit))