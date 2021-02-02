# Programmers - Lv1 - Uncompleted participant
def solution(participant, completion):
    participant.sort()
    completion.sort()

    for p, c in zip(participant, completion):
        if p != c:
            return p
    
    return participant.pop()

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

participant2 = ["mislav", "stanko", "mislav", "ana"]
completion2 = ["stanko", "ana", "mislav"]
print(solution(participant2, completion2))