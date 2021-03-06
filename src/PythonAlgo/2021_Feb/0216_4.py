# Programmers - Lv2 - Bracket Translation
def solution(p):    
    if correct(p):
        return p
    else:
        return recursive(p)

def correct(p):
    stack = []
    for i in p:
        if i == '(':
            stack.append(i)
        elif stack:
            stack.pop()

    return not bool(stack) 

def recursive(p):
    if p == '':
        return ''
    u, v = divide(p)
    if correct(u):
        return u + recursive(v)
    else:
        return '('+recursive(v)+')'+change(u)
    
def change(p):
    p = p[1:-1]
    return ''.join(['(' if c==')' else ')' for c in p])

def divide(p):
    l_num = 0
    r_num = 0
    u = ''
    v = ''
    for i in range(0, len(p)):
        if p[i] == '(':
            l_num += 1
            u += p[i]
        elif p[i] == ')':
            r_num += 1
            u += p[i]

        if l_num == r_num and i < len(p)-1:
            v = p[i+1:]
            break
    
    return u, v

p = "(()())()"
p2 = ")("
p3 = "()))((()"
print(solution(p3))