# Programmers - Lv2 - Calculation Maximize
from itertools import permutations
from re import split

def solution(expression):
    answer = 0
    # *+-로 조합 만들기(총 3!=6가지).
    operands = permutations(['*', '+', '-'])
    # 6가지 경우에 대해 체크
    for op in operands:
        # 숫자만, 연산자만 따로 list로
        nums = split('[*+-]', expression)
        ops = split('[0-9]+', expression)[1:-1]
        # 한가지 조합 경우 내에서(우선 순위 첫번째부터 시작)
        for i in op[:2]:
            # 주어진 식에 있는 연산자일때 해당 연산자의 앞뒤 숫자들 계산 먼저 한 후
            while i in ops:
                idx = ops.index(i)
                tmp = nums[idx]+ops[idx]+nums[idx+1]
                # 이미 사용한건 pop 새로 계산한 건 집어넣기
                nums[idx] = str(eval(tmp))
                nums.pop(idx+1)
                ops.pop(idx)
        
        # 마지막 계산 한번 처리
        tmp = ''
        for i in range(len(ops)):
            tmp += nums[i]+ops[i]
        
        # 절댓값 적용 & 최댓값 뽑기
        tmp = abs(eval(tmp + nums[-1]))
        if tmp > answer:
            answer = tmp

    return answer

expression = "100-200*300-500+20"
print(solution(expression))