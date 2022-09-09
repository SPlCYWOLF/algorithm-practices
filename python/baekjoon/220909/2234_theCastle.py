from collections import deque
import sys
sys.stdin = open('input.txt')

# bfs돌면서 가장 넓은 방 저장
# bfs다 돌면 방 개수 + 1
# 해당 방의 넓이는 area_record = dict() 에 저장해 놓음

# 방을 조합해서 최대 합의 방이 정답

# 남 동 북 서 (하-> 우-> 상-> 좌)
dr = (1, 0, -1, 0)
dc = (0, 1, 0, -1)

def bfs(r, c):
    Q = deque()
    Q.append((r, c))
    area = 1
    while Q:
        r, c = Q.popleft()
        if len(bin(castle[r][c])) 
        walls = bin(castle[r][c])[2::]
        for k in range(4):
            if walls[k] == "0":
                nr, nc = r + dr[k], c + dc[k]
                if not visited[nr][nc]:
                    visited[nr][nc] = 1
                    area += 1
                    Q.append((nr, nc))
    return area





M, N = map(int, input().split())
castle = tuple(tuple(map(int, input().split())) for _ in range(N))

area_record = dict()

visited = [[0] * M for _ in range(N)]
room_num = 1
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            visited[i][j] = 1
            area_record[room_num] = bfs(i, j)
            room_num += 1

largest_area = max(area_record, key=area_record.get)
print(largest_area)