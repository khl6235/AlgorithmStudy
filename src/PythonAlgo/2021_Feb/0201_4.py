# Programmers - Lv1 - Free Sorting
def solution(strings, n):
    answer = sorted(sorted(strings), key=lambda strings: strings[n])
    return answer

strings = ["sun", "bed", "car"]
strings2 = ["abce", "abcd", "cdx"]
print(solution(strings, 1))