import sys
sys.stdin = open('input.txt')

# 출처 https://seongonion.tistory.com/108
# 총 투자 시간 40분
n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [0] * (k+1)
dp[0] = 1
# dp[i] -> i원을 만들 때 가능한 경우의 수
# dp[0] -> 동전 하나를 사용하는 경우 (coin이 3일 때, dp[3 - 3] = 1로 맞춰줌으로써 0원에서 3원을 더해 3원을 만드는 경우라고 생각)

dp[5] = dp[5] + dp[3]
for coin in coins:
    for i in range(coin, k+1):
        # coin원 동전으로 i원 만들기 -> i - coin원을 만든 후 coin원을 추가하는 것과 같음
        # 즉, coin원으로 동전을 만드는 경우의 수 -> dp[i - coin]원
        possible_cases = dp[i - coin]
        dp[i] += possible_cases

print(dp[k])






# 패작 1
# def dfs(target, nums):
#     global ans
#     if sum(tmp) == k and tmp not in used:
#         used.append(sorted(tmp))
#         ans += 1
#     else:
#         for i in range(len(nums)):
#             tmp.append(nums[i])
#             dfs(nums[i], nums)
#             tmp.pop(-1)
#
# dfs(nums[0], nums)