# Programmers - Lv2 - Pair Removal
def solution(s):
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop(-1)
        else:
            stack.append(i)

    return 1 if len(stack) == 0 else 0

s = "baabaa"
s2 = "cdcd"
print(solution(s))