# BOJ - DP - Sugar Delivery
N = int(input())
answer = 0

while True:
    if N % 5 == 0:
        answer += (N//5)
        break
    elif N < 0:
        answer = -1
        break
    N -= 3
    answer += 1

print(answer)