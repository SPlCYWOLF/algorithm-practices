import sys
sys.stdin = open('input.txt')

# 실패 : 틀렸음
N = int(sys.stdin.readline())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [0] * (N+1)

for i in range(N):
    t, p = table[i]

    if t + i > N:   # N+1 일째부터는 회사가 없어 상담 불가
        continue

    dp[i + t] = max(dp[i + t], dp[i] + p) # 다음에 일할 수 있는 날에 받은 pay를 입력

    dp[i + 1] = max(dp[i + 1], dp[i])     # 각각 시작한 위치를 다르게 잡아서 pay가 가장 큰 것을 기록

print(dp)



# 성공
# N = int(input())
# table = [list(map(int, input().split())) for _ in range(N)]
#
# dp = [0] * (N+1)
#
# largest = 0
# for i in range(N):
#     t, p = table[i]
#     largest = max(largest, dp[i])
#
#     if t + i > N:   # N+1 일째부터는 회사가 없어 상담 불가
#         continue
#
#     dp[i+t] = max(largest + p, dp[i+t])
#
# print(max(dp))