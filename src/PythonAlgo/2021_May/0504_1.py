# Programmers - Hash - uncompleted athletes
def solution(participant, completion):
    dict_p = {}
    for p in participant:
        if p in dict_p:
            dict_p[p] = dict_p.get(p) + 1
        else:
            dict_p[p] = 1

    for c in completion:
        if c in dict_p:
            dict_p[c] = dict_p.get(c) -1

    return [k for k, v in dict_p.items() if v == 1].pop()

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))