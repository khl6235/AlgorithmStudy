# Programmers - Lv2 - English word game
def solution(n, words):
    answer = [0, 0]
    for i in range(len(words)):
        if words[i] in words[:i]:
            return [i%n+1, i//n+1]
        elif i>0 and words[i-1][-1] != words[i][0]:
            return [i%n+1, i//n+1]
    return answer

n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
n2 = 2
words2 = ["hello", "one", "even", "never", "now", "world", "draw"]
print(solution(n2, words2))