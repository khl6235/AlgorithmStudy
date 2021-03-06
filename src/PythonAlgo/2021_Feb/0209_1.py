# Programmers - Lv1 - Press Keypad
def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12
    for n in numbers:
        if n == 1 or n == 4 or n == 7:
            left = n
            answer += 'L'
        elif n == 3 or n == 6 or n == 9:
            right = n
            answer += 'R'
        else:
            n = 11 if n == 0 else n

            absL = abs(n-left)
            absR = abs(n-right)

            if sum(divmod(absL, 3)) > sum(divmod(absR, 3)):
                right = n
                answer += 'R'
            elif sum(divmod(absL, 3)) < sum(divmod(absR, 3)):
                left = n
                answer += 'L'
            else:
                if hand == "right":
                    right = n
                    answer += 'R'
                elif hand == "left":
                    left = n
                    answer += 'L'

    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
numbers2 = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "right"
hand2 = "left"
print(solution(numbers, hand))