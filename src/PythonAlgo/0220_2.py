# Programmers - Lv2 - H Index
def solution(citations):
    citations = sorted(citations)
    print(citations)
    for i in range(0, len(citations)):
        if len(citations)-i <= citations[i]:
            return len(citations)-i
    
    return 0

citations = [3, 0, 6, 1, 5]
citations2 = [0, 0, 0]
citations3 = [3, 3, 3, 3]
print(solution(citations2))