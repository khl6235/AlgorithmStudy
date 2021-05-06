# Programmers - Sorting - H Index
def solution(citations):
    citations.sort()
    length = len(citations)
    for i in range(length):
        if length-i <= citations[i]:
            return length-i
    return 0

citations = [3, 0, 6, 1, 5]
print(solution(citations))