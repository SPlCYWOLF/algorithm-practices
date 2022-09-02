from collections import deque
import sys
sys.stdin = open('input.txt')

# bfs 돌면서 q 들어갈때 마다 해당 이동지의 시간 + 1를 이동 경로와 함께 관리
# 현재 rat보다 크지않은 숫자는 무시, 아니라면 먹고 + 1

# 먹은 개수 카운트, N과 같아지면 해당 이동 경로값을 min_travel에 저장
# 남은 Q들도 도는데, 만약 min_travel보다 이동시간 값이 같거나 높아지면 즉각 종료

# 시작점에서 시작해서 아무 치즈나 도착 하면 total_time에 이동거리 축적, visited 초기화, 먹은 치즈 반영,
# 해당 도착 치즈를 출발점으로 다시 bfs반복하여 먹은 치즈 개수가 N과 같아지면 종료

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

def bfs(r, c):
    visited = [[0] * W for _ in range(H)]
    visited[r][c] = 1
    Q = deque()
    Q.append((r, c, 0))
    while Q:
        r, c, t = Q.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]

            if 0 <= nr < H and 0 <= nc < W:
                if not visited[nr][nc]:
                    if field[nr][nc] != "X":
                        t += 1
                        if field[nr][nc] == ".":
                            visited[nr][nc] = 1
                            Q.append((nr, nc, t))
                            t -= 1
                            continue
                        if int(field[nr][nc]) <= rat:
                            field[nr][nc] = "."
                            return nr, nc, t
                        else:
                            visited[nr][nc] = 1
                            Q.append((nr, nc, t))
                            t -= 1


H, W, N = map(int, input().split())
field = [list(input()) for _ in range(H)]

new_start = []
rat, total_time = 1, 0
for i in range(H):
    for j in range(W):
        if field[i][j] == "S":
            field[i][j] = "."
            new_start = [i, j]
            break
    if new_start:
        break

while rat < N+1:
    new_start[0], new_start[1], time = bfs(new_start[0], new_start[1])
    total_time += time
    rat += 1

print(total_time)
