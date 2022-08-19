# 테두리 칸 제외, 모든 칸 돌며 각 칸마다 bfs 시작

# 매 bfs 마다 상 우 하 좌 순으로 본인보다 크지만 가장 낮은 벽 높이 저장하며 진행
# 상하좌우 확인하며 본인과 같거나 작으면 bfs 진행
# visited도 여기서 체크 후 높이 매게변수 리스트에 저장하며 bfs 진행
# but! 이미 visited 체크 되어있다해도 bfs들어가지만, 높이 저장 안함

# 본인 높이보다 높으면 bfs 안 들어감

# 마지막에 상하좌우에서 가장 작은 벽 높이 - 각 저장된 매게변수 리스트의 각 높이 의 총 값 ans에 축적

# bfs돌다가 한 곳이라도 테두리 값이 본인거보다 작으면, 종료 (물 다샘)

# 새로운 bfs들어갈때는 visited

# 반복

from collections import deque
import sys
sys.stdin =open('input.txt')

# 상 우 하 좌
dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

def seperate(nums):
    temp = [*nums]
    return map(int, temp)

def bfs(r, c):
    heights, min_wall = [field[r][c]], 9999999999
    test_visited = []
    Q = deque()
    Q.append([r, c])
    while Q:
        r, c = Q.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]

            if [nr, nc] not in test_visited and field[r][c] < field[nr][nc]:
                min_wall = min(min_wall, field[nr][nc])
                continue

            if nr == 0 or nr == N-1 or nc == 0 or nc == M-1:
                return 0

            if field[r][c] >= field[nr][nc]:
                if [nr, nc] not in test_visited:
                    test_visited.append([nr, nc])
                    Q.append([nr, nc])
                    if not visited[nr][nc]:
                        heights.append(field[nr][nc])
                continue

    for v in test_visited:
        r, c = v
        visited[r][c] = 1

    temp = 0
    for h in heights:
        temp += min_wall - h

    return temp


N, M = map(int, input().split())
field = [tuple(seperate(input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

print(field)
ans = 0
for i in range(1, N-1):
    for j in range(1, M-1):
        if not visited[i][j]:
            visited[i][j] = 1
            ans += bfs(i, j)

print(ans)