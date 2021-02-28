# Programmers - Lv2 - Tuple
def solution(s):
    answer = []
    s = s[2:-2].split("},{")
    s.sort(key=len)
    
    for i in s:
        tmp = i.split(',')
        for j in tmp:
            if int(j) not in answer:
                answer.append(int(j))
    
    return answer

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
s2 = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
s3 = "{{20,111},{111}}"
print(solution(s2))