import sys
sys.stdin = open('input.txt')

# thought process:
# 그냥 위 1(N극)을 발견하고 아직 방문기록이 없으면, 해당 지점을 기준으로 계속
# 세로로 내려다가(한번 방문을 하면 방문기록을 남긴다),
# 2(S극) 을 찾으면 그대로 강제 루프 종료 후, 처음 세로로 내려가기 시작한
# 지점으로 돌아가는 반복작업을 한다.

# 소요시간 약 2시간.
for tc in range(1, 11):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1 and visited[i][j] == 0:
                for k in range(i, N):
                    if arr[k][j] == 2:
                        cnt += 1
                        break
                    visited[k][j] = 1
    print('#{} {}'.format(tc, cnt))