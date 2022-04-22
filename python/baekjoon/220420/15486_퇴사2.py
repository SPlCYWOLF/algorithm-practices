# 2차원 배열로 이동 횟수마다 얻은 이익을 저장
# BFS로 가자
# 종료 조건은, 일 수가 더이상 남지 않으면 종료

# follow along 해야하는 값들:
#   - 남은 일자
#   - 축적되는 이익


# 30분시간 지나서 일단 다른사람 코드로 배우기 위해 스크랩
# 60분 추가로 봐도 아직 이해 못함
import sys

N = int(sys.stdin.readline())

day = N
T, P = [], []
dp = [0] * (N + 1)

for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    T.append(temp[0])
    P.append(temp[1])

for i in range(0, N):
    if T[i] <= N - i:
        dp[i + T[i]] = max(dp[i + T[i]], dp[i] + P[i])

    dp[i + 1] = max(dp[i + 1], dp[i])

print(dp[N])