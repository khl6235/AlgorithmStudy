# Programmers - Lv2 - News Clustering
def solution(str1, str2):
    answer = 1
    set1 = list()
    set2 = list()
    for i in range(len(str1)-1):
        s = letter_check(str1[i:i+2])
        if s:
            set1.append(s)
    for i in range(len(str2)-1):
        s = letter_check(str2[i:i+2])
        if s:
            set2.append(s)
    
    if set1 and set2:
        if len(set1) >= len(set2):
            its = [set1.remove(x) for x in set2 if x in set1]
        else:
            its = [set2.remove(x) for x in set1 if x in set2]
        tmp = set1+set2
        uni = len(tmp)
        if uni == 0:
            answer = 1
        else:
            answer = len(its)/uni

    return int(answer*65536)

def letter_check(s):
    for l in s:
        if 65 <= ord(l) <= 90 or 97 <= ord(l) <= 122:
            continue
        else:
            return False
    return s.lower()

str1 = "FRANCE"
str2 = "french"
str11 = "handshake"
str22 = "shake hands"
str111 = "aa1+aa2"
str222 = "AAAA12"
str1111 = "E=M*C^2"
str2222 = "e=m*c^2"
print(solution("aaa", "bbb"))