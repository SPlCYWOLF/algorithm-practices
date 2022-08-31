from collections import deque
import sys
sys.stdin = open('input.txt')
# bfs로 가장 큰 blob 탐색 하며 해당 blob의 perimeter도 기록
# 가장 큰 blob 너비 기록
# 가장 큰 blob와 동일한 기록이 나오면 더 작은 perimeter를 출력
# perimeter 확인 여부는, Q에 들어가는 조건이 아니면 무조건 +1

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

def bfs(r, c):
    global largest_perimeter, visited
    visited[r][c] = 1
    area, perimeter = 1, 0
    Q = deque()
    Q.append((r, c))
    while Q:
        r, c = Q.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if not visited[nr][nc]:
                    if icecream[nr][nc] == "#":
                        visited[nr][nc] = 1
                        Q.append((nr, nc))
                        area += 1
                    else:
                        perimeter += 1
            else:
                perimeter += 1

    if area == largest_blob:
        largest_perimeter = min(largest_perimeter, perimeter)
    elif area > largest_blob:
        largest_perimeter = perimeter

    return area


N = int(input())
icecream = [list(input()) for _ in range(N)]
largest_blob, largest_perimeter = 0, 0

visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j] and icecream[i][j] == "#":
            largest_blob = max(largest_blob, bfs(i, j))

print(largest_blob, largest_perimeter)