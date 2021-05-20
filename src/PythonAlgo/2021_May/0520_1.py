# BOJ - DP - 2xn Tiling
n = int(input())
dp = [0]*(n+1)
dp[0] = 1
dp[1] = 1

def calc(n):
    for i in range(2, n+1):
        dp[i] = dp[i-1]+dp[i-2]
        dp[i] %= 10007

    return dp[n]

print(calc(n))