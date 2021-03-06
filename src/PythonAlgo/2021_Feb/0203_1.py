# Programmers - Lv1 - PreExam
def solution(answers):
    answer = []
    res = [0, 0, 0]
    ans1 = []
    ans2 = []
    ans3 = []
    for i in range(0, len(answers)):
        ans1.append((i%5)+1)
        if i%2 == 0:
            ans2.append(2)
        else:
            ans2.append(two(i%8))
        ans3.append(three(i%10))

    for i in range(0, len(answers)):
        if answers[i] == ans1[i]:
            res[0] += 1
        if answers[i] == ans2[i]:
            res[1] += 1
        if answers[i] == ans3[i]:
            res[2] += 1

    max_num = max(res)
    for n in range(3):
        if res[n] == max_num:
            answer.append(n+1)

    return answer

def two(x):
    return{ 1:1, 3:3, 5:4, 7:5 }[x]

def three(x):
    return{ 0:3, 1:3, 2:1, 3:1, 4:2, 5:2, 6:4, 7:4, 8:5, 9:5 }[x]

answers = [1,2,3,4,5]
answers2 = [1,3,2,4,2]
print(solution(answers))