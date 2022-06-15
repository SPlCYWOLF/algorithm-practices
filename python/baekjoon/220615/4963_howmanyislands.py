import sys
from collections import deque
sys.stdin = open('input.txt')

# 지도 생성 & 방문 체크
# BFS로 지도 돌면서 방문하며 visited 체크
# BFS 루프 끊기면 cnt + 1
# 모두 방문하면 끝

#   상 상우 우 우하 하 좌하 좌 좌상

def bfs(start):
    deq = deque()
    deq.append(start)
    while deq:
        r, c = deq.popleft()
        for k in range(8):
            nr = r + dy[k]
            nc = c + dx[k]
            if 0 <= nr < h and 0 <= nc < w and the_map[nr][nc] == 1 and not v_map[nr][nc]:
                v_map[nr][nc] = 1
                deq.append([nr, nc])


dx = (0, 1, 1, 1, 0, -1, -1, -1)
dy = (-1, -1, 0, 1, 1, 1, 0, -1)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    the_map = [list(map(int, input().split())) for _ in range(h)]   # 지도 생성
    v_map = [[0] * w for _ in range(h)]                             # visited 생성

    cnt = 0

    for i in range(h):
        for j in range(w):
            if the_map[i][j] == 1 and not v_map[i][j]:
                v_map[i][j] = 1
                bfs([i, j])
                cnt += 1

    print(cnt)



