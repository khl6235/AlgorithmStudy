# BOJ - DP - Fibonacci
T = int(input())

def cal(N):
    dp = [(0, 0)]*(N+1)
    dp[0] = (1, 0)
    dp[1] = (0, 1)
    for i in range(2, N+1):
        dp[i] = (dp[i-1][0]+dp[i-2][0], dp[i-1][1]+dp[i-2][1])
    
    return str(dp[-1][0])+" "+str(dp[-1][1])

for _ in range(T):
    N = int(input())
    if N == 0:
        print("1 0")
    else:
        print(cal(N))