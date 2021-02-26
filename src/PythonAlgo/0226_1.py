# Programmers - Lv2 - Rank Search
from itertools import combinations
from collections import defaultdict
def solution(info, query):
    answer = []
    group = defaultdict(list)
    for i in info:
        spl = i.split()
        words = spl[:-1]
        score = int(spl[-1])
        for j in range(5):
            for c in list(combinations(words, j)):
                tmp = ''.join(c)
                group[tmp].append(score)
        
    # group = dict(sorted(group.items(), reverse=True, key= lambda x:x[1]))
    # 미리 오름차순 정렬 해두기. 아래 query 에서 정렬하면 시간 초과!
    for key in group.keys():
        group[key].sort()

    for q in query:
        q = q.split()
        q_score = int(q[-1])
        q = q[:-1]
        tmp = ''
        for w in q:
            if w != 'and' and w != '-':
                tmp += w
        print(tmp)
        if tmp in group:
            score_info = group[tmp]
            print(score_info, q_score)
            l = len(score_info)
            if l > 0:
                start, end = 0, l
                while end > start:
                    mid = (start+end)//2
                    if score_info[mid] >= q_score:
                        end = mid
                    else:
                        start = mid+1
                    print(start, mid, end)

                answer.append(l - start)
        else:
            answer.append(0)

    return answer

info = ["java backend junior pizza 150",
"python frontend senior chicken 210",
"python frontend senior chicken 150",
"cpp backend senior pizza 260",
"java backend junior chicken 80",
"python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100",
"python and frontend and senior and chicken 200",
"cpp and - and senior and pizza 250",
"- and backend and senior and - 150",
"- and - and - and chicken 100",
"- and - and - and - 150"]

print(solution(info, query))