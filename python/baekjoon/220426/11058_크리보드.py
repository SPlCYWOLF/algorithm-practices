import sys
sys.stdin = open('input.txt')

# 30분 소요 이해 못함
# 출처 https://jokerkwu.tistory.com/172
n = int(input())
dp = [i for i in range(0, 102)]

for i in range(6, 101):
    dp[i] = max(dp[i-3]*2, max(dp[i-4]*3, dp[i-5]*4))
print(dp[n])