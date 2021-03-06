# Programmers - Lv2 - String compression
def solution(s):
    answer = len(s)
    for num in range(1, len(s)//2+2):
        tmp_s =''
        i = 0
        cnt = 1
        while i < len(s):
            if s[i:i+num] == s[i+num:i+num*2]:
                cnt += 1
            elif cnt > 1:
                tmp_s += str(cnt) + s[i:i+num]
                cnt = 1
            else:
                tmp_s += s[i:i+num]
                cnt = 1
            
            i += num
        
        if len(tmp_s) < answer:
            answer = len(tmp_s)
    return answer

s = "aabbaccc"
s2 = "ababcdcdababcdcd"
print(solution(s))