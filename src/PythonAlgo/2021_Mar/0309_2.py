# Programmers - Lv2 - Repeating Binary
def solution(s):
    length = len(s)
    answer = [0, 0]
    while length > 1:
        answer[0] += 1
        s = s.replace("0", "")
        answer[1] += length - len(s)
        s = binary(len(s))
        length = len(s)
    
    return answer

def binary(n):
    res = ""
    while n > 1:
        res += str(n%2)
        n = n//2
    if n == 1:
        res += "1"

    return res


s = "110010101001"
s2 = "01110"
s3 = "1111111"
print(solution(s3))