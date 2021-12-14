import sys
sys.stdin = open('input.txt')

# 49/51 통과
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

def dfs(r, c, t, skill):
    global ans
    visited[r][c] = 1

    # 4. 가장 긴 이동 길이를 기록해서 ans 에 업데이트
    if t > ans:
        ans = t

    if road[r][c] != 0:              # 해당 위치 높이가 0일때는 미 실행
        for w in range(4):
            nr = r + dr[w]
            nc = c + dc[w]

            # 3. K 값만큼 깍을 수 있고, 백트래킹으로 갔던 길 원상복구도 시켜야 하고, visited도 언체크 해야함
            if 0 <= nr < N and 0 <= nc < N:
                if not visited[nr][nc]:
                    if road[r][c] > road[nr][nc]:
                        dfs(nr, nc, t+1, skill)
                        visited[nr][nc] = 0
                    elif road[r][c] > road[nr][nc] - skill:
                        temp = road[nr][nc]
                        road[nr][nc] = road[r][c] - 1
                        dfs(nr, nc, t+1, 0)
                        road[nr][nc] = temp
                        visited[nr][nc] = 0
            
for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    road = [list(map(int, input().split())) for _ in range(N)]
    ans = 1
    # 1. 최고 높이 봉우리 찾고
    highest = max(map(max, road))
    # 2. 그걸 기준으로 dfs 돌리는데,
    for i in range(N):
        for j in range(N):
            if road[i][j] == highest:
                visited = [[0]*N for _ in range(N)]
                dfs(i, j, 1, K)    # 위치, 이동 거리, 깍기 스킬

    print('#{} {}'.format(tc, ans))