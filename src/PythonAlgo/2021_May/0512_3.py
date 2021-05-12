# BOJ - DP - Adding 1,2,3
T = int(input())

def cal(N):
    if N == 1:
        return 1
    elif N == 2:
        return 2
    elif N == 3:
        return 4
    else:
        return cal(N-1)+cal(N-2)+cal(N-3)

for _ in range(T):
    N = int(input())
    print(cal(N))