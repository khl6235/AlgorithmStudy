# Programmers - Hash - Best Album
from collections import defaultdict
def solution(genres, plays):
    answer = []
    dict_g = defaultdict(list)
    dict_p = defaultdict(int)
    i = 0
    for g, p in zip(genres, plays):
        dict_p[i] = p
        dict_g[g].append(dict_p[plays.index(p)])
        i += 1

    dict_g = sorted(dict_g.items(), key=lambda x:sum(x[1]), reverse=True)

    dict_p2 = defaultdict(list)
    for k, v in dict_p.items():
        dict_p2[v].append(k)

    for _, v in dict_g:
        v = sorted(v, key=lambda x:x, reverse=True)
        for vv in v[:2]:
            for k1, v1 in dict_p2.items():
                if k1==vv:
                    answer.append(v1[0])
                    v1.pop(0)
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
genres2 = ["classic", "pop", "classic", "pop", "classic", "classic"]
plays2 = [400, 600, 150, 600, 500, 500]
print(solution(genres, plays))