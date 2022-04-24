# 2차원 배열로 이동 횟수마다 얻은 이익을 저장
# BFS로 가자
# 종료 조건은, 일 수가 더이상 남지 않으면 종료

# follow along 해야하는 값들:
#   - 남은 일자
#   - 축적되는 이익


# 30분시간 지나서 일단 다른사람 코드로 배우기 위해 스크랩
# 30분 추가로 봐도 아직 이해 못함
import sys

N = int(sys.stdin.readline())       # 왜 sys & stdin & readline() 쓰는걸까?

day = N
T, P = [], []
dp = [0] * (N + 1)

for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    T.append(temp[0])
    P.append(temp[1])

for i in range(0, N):
    if T[i] <= N - i:       # 일할 날이 남아있는 경우
        dp[i + T[i]] = max(dp[i + T[i]], dp[i] + P[i])      # 다음에 일할 수 있는 날에 받은 pay를 입력

    dp[i + 1] = max(dp[i + 1], dp[i])                       # 각각 시작한 위치를 다르게 잡아서 pay가 가장 큰 것을 기록
print(dp[N])                                                # 마지막 날에 받게되는 최고 pay.