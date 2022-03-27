import sys
sys.stdin = open('input.txt')


readline = sys.stdin.readline

N = int(readline().rstrip())

grid = [[2] * (N + 2)] + [[2] + list(map(int, readline().rstrip().split())) + [2] for _ in range(N)] + [[2] * (N + 2)]  # 지도 받기
# 파이프 경우의 수. 0이면 가로 방향으로 온 경우의 수, 2면 세로 방향으로 온 경우의 수, 1이면 대각선 방향으로 온 경우의 수
lst = [[(0, 0, 0)] * (N + 2) for _ in range(N + 2)]
lst[1][2] = (1, 0, 0)

for r in range(1, N + 1):
    for c in range(3, N + 1):
        if grid[r][c] != 0:  # 벽이라면 자동으로 모든 경우의 수가 (0, 0, 0)
            continue

        if grid[r - 1][c] + grid[r][c - 1] + grid[r][c] == 0:  # 1번 방향으로 올 경우의 수
            lst[r][c] = (lst[r][c][0], sum(lst[r - 1][c - 1]), lst[r][c][2])

        lst[r][c] = (lst[r][c - 1][0] + lst[r][c - 1][1], lst[r][c][1], lst[r][c][2])

        lst[r][c] = (lst[r][c][0], lst[r][c][1], lst[r - 1][c][1] + lst[r - 1][c][2])

print(sum(lst[N][N]))





# 3차 시도 실패 소요 시간 40분
# 오타 발견으로 해결하나 싶었지만, 시간초과.
# 정답은 나오는걸로 확인됨
# 고로 다른 접근법: BFS활용하여 재도전


N = int(input())
road = [list(map(int, input().split())) for _ in range(N)]
ans = 0
# 2차 시도 소요시간 40분 실패
# 방향 델타값 활용 (구별해서 dfs 진입)
#   - 가로일때 우, 우하
#   - 세로일때 하, 우하
#   - 대각선때 우, 우하, 하
# 백트래킹 할 필요 x
# 왓던곳으로 다시 돌아갈 걱정 안해도 됨

# 파이프 상태 가로일때
dr_r = (0, 1)
dc_r = (1, 1)
# 파이프 상태 세로일때
dr_c = (1, 1)
dc_c = (0, 1)
# 파이프 상태 대각선일때
dr_d = (0, 1, 1)
dc_d = (1, 1, 0)

# 0 = 가로  ,  1 = 대각선  ,  2 = 세로

def dfs(r, c, p):
    global ans

    if r+1 == N and c+1 == N:
        ans += 1

    elif p == 0:
        for i in range(2):
            nr = r+dr_r[i]
            nc = c+dc_r[i]

            if 0 <= nr < N and 0 <= nc < N:
                if i == 0 and road[nr][nc] == 0:
                    dfs(nr, nc, 0)
                elif i == 1 and road[nr][nc] + road[nr-1][nc] + road[nr][nc-1] == 0:
                    dfs(nr, nc, 1)
    elif p == 1:
        for i in range(3):
            nr = r + dr_d[i]
            nc = c + dc_d[i]

            if 0 <= nr < N and 0 <= nc < N:
                if i == 0 and road[nr][nc] == 0:
                    dfs(nr, nc, 0)
                elif i == 1 and road[nr][nc] + road[nr-1][nc] + road[nr][nc-1] == 0:
                    dfs(nr, nc, 1)
                elif i == 2 and road[nr][nc] == 0:
                    dfs(nr, nc, 2)
    elif p == 2:
        for i in range(2):
            nr = r+dr_c[i]
            nc = c+dc_c[i]

            if 0 <= nr < N and 0 <= nc < N:
                if i == 0 and road[nr][nc] == 0:
                    dfs(nr, nc, 2)
                elif i == 1 and road[nr][nc] + road[nr-1][nc] + road[nr][nc-1] == 0:
                    dfs(nr, nc, 1)

dfs(0, 1, 0)    # row, column, position

print(ans)









# 1차 시도 소요시간 30분
# dfs 로 풀면 될듯 함
# 파이프는 최소 2개의 빈칸을 차지함 => 회전 시키면 기존 한칸에서 벗어나서 다른 한칸을 차지하게됨
# => 도데체 어떤 기준으로 새로운 한칸을 차지하게 되는지 모르겠음 => 회전 기준을 알려줘야함
#