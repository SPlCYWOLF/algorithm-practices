import sys
sys.stdin = open('input.txt')

# 증가하는 부분수열 값 = 증부값
A = int(input())
nums = list(map(int, input().split()))
dp = [0] * A

for i in range(A):              # 각 원소를 기준으로 앞의 원소의 크기와 비교
    for j in range(A):
        if nums[i] > nums[j] and dp[i] < dp[j]: # 현재 원소가 기준 원소보다 크다면, 증부값 확인 후
            dp[i] = dp[j]       # 최대 증부값 dp에 갱신
    dp[i] += 1                  # 각 원소는 최소 1의 증부값임으로 +1

print(max(dp))

