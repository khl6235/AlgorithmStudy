# Programmers - Lv2 - Right Bracket
def solution(s):
    return correct(s)

def correct(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        elif stack:
            stack.pop()
        elif i == ')':
            return False
    return not bool(stack) 

s = "()()"
s2 = "(())()"
s3 = ")()("
s4 = "(()("
print(solution(s))