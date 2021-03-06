# Programmers - Lv1 - Weird word
def solution(s):
    res = []
    word = s.split(" ")
    for w in word:
        new_word = ''
        for i in range(0, len(w)):
            if i%2 == 0:
                new_word += w[i].upper()
            else:
                new_word += w[i].lower()

        res.append(new_word)
    
    return ' '.join(res)

s = "try hello world"
s1 = "dd   adb"
print(solution(s))