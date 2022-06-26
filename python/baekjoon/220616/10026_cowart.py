import sys
from collections import deque
sys.stdin = open('input.txt')

# BFS 활용하여 색 영역 확인
# 일단은 사람 따로 소 따로 해답 구해보기

def human_bfs(start, color):
    deq = deque()
    deq.append(start)

    while deq:
        r, c = deq.popleft()

        for k in range(4):
            nr = r + dy[k]
            nc = c + dx[k]

            if 0 <= nr < N and 0 <= nc < N and not visited_human[nr][nc] and color == canvas[nr][nc]:
                visited_human[nr][nc] = 1
                deq.append([nr, nc])

def cow_bfs(start, color):
    deq2 = deque()
    deq2.append(start)

    while deq2:
        r, c = deq2.popleft()

        for k in range(4):
            nr = r + dy[k]
            nc = c + dx[k]

            if 0 <= nr < N and 0 <= nc < N and not visited_cow[nr][nc]:
                if color == canvas[nr][nc]:
                    visited_cow[nr][nc] = 1
                    deq2.append([nr, nc])
                elif color == "G" and canvas[nr][nc] == "R":
                    visited_cow[nr][nc] = 1
                    deq2.append([nr, nc])
                elif color == "R" and canvas[nr][nc] == "G":
                    visited_cow[nr][nc] = 1
                    deq2.append([nr, nc])


dx = (0, 1, 0, -1)
dy = (-1, 0, 1, 0)

N = int(input())
canvas = [list(input()) for _ in range(N)]
visited_human = [[0] * N for _ in range(N)]
visited_cow = [[0] * N for _ in range(N)]
human_cnt, cow_cnt = 0, 0

for i in range(N):
    for j in range(N):
        if not visited_human[i][j]:
            visited_human[i][j] = 1
            human_bfs([i, j], canvas[i][j])
            human_cnt += 1
        if not visited_cow[i][j]:
            visited_cow[i][j] = 1
            cow_bfs([i, j], canvas[i][j])
            cow_cnt += 1

print(human_cnt, cow_cnt)
