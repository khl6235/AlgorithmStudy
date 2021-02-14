# Programmers - Lv2 - Stock Price
# Stack
def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = [0]
    for s in range(1, len(prices)):
        while stack and prices[stack[-1]] > prices[s]:
            tmp = stack.pop()
            answer[tmp] = s - tmp
            
        stack.append(s)
        
    for st in stack:
        answer[st] = len(prices)-1 - st

    return answer

prices = [1, 2, 3, 2, 3]
print(solution(prices))