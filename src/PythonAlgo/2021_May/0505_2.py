# Programmers - Stack/Queue - Stock Price
def solution(prices):
    answer = [0]*len(prices)
    stack = [0] # 시간 저장용 스택
    for i in range(1, len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            tmp = stack.pop()
            answer[tmp] = i - tmp
        stack.append(i)

    for i in range(len(answer)):
        if answer[i] == 0:
            answer[i] = len(prices)-1 - i

    return answer

prices = [1, 2, 3, 2, 3]
print(solution(prices))