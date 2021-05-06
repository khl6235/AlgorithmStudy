# Programmers - DP - N Expressing
def solution(N, number):
    answer = -1
    dp = []

    for i in range(1, 9):
        all = set()
        check = int(str(N)*i)
        all.add(check)
        for j in range(0, i-1):
            for op1 in dp[j]:
                for op2 in dp[-j-1]:
                    all.add(op1+op2)
                    all.add(op1-op2)
                    all.add(op1*op2)
                    if op2 != 0:
                        all.add(op1//op2)
        if number in all:
            answer = i
            break
        dp.append(all)

    return answer

N = 5
number = 12
print(solution(N, number))