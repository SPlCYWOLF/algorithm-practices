import sys
sys.stdin = open('input.txt')


N = int(input())
dp = [0] * 21
dp[1] = 1

for i in range(2, N+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[N])