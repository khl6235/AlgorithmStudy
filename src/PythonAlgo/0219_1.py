# Programmers - Lv2 - Large Number
def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while k > 0 and stack and stack[-1] < num:
            stack.pop(-1)
            k -= 1
        stack.append(num)
    
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)

number = "1924"
k = 2
number2 = "1231234"
k2 = 3
number3 = "4177252841"
k3 = 4
print(solution(number3, k3))