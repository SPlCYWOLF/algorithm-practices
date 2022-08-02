from collections import deque
import sys
sys.stdin = open('input.txt')

# D값을 이진탐색법으로 줄이거나 늘려나가며 D값 탐색
# 각 mid 값으로 BFS돌며, 다 돌았을때 waypoint가 방문되어있는지 여부 확인
# BFS방문 가능 여부는 visited 와 mid값으로 정의
# waypoint 모두 방문했으면 해당 mid값 ans에 저장,
# r = mid - 1 로 조정 후 새로운 mid값으로 bfs시작
# 방문 불가능 했으면, l = mid + 1로 조정 후 다시 bfs시작

#    상 우 하 좌
dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

def bfs(m):

    Q = deque()
    Q.append((1, 1))
    while Q:
        r, c = Q.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            difference = abs(elevations[r][c] - elevations[nr][nc])
            if difference <= m and not visited[nr][nc]:
                Q.append((nr, nc))
                visited[nr][nc] = 1

    for wp in waypoints:
        wr, wc = wp
        if not visited[wr+1][wc+1]:
            return False

    return True


M, N = map(int, input().split())
elevations = [[9999999999]*(N+2)] + [[9999999999] + list(map(int, input().split())) + [9999999999] for _ in range(M)] + [[9999999999]*(N+2)]

waypoints = []
temp = [list(map(int, input().split())) for _ in range(M)]
for i in range(M):          # waypoints 위치 값 저장
    for j in range(N):
        if temp[i][j]:
            waypoints.append((i, j))
highest = 0
for i in range(1, M):
    for h in elevations[i][1:N]:
        highest = max(highest, h)

D = 0

l, r = 0, highest
while l <= r:
    mid = (l + r) // 2
    visited = [[0] * (N+2) for _ in range(M+2)]

    if bfs(mid):
        D = mid
        r = mid - 1
    else:
        l = mid + 1

print(D)