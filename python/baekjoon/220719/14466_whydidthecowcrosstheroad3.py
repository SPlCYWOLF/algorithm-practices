# 벽 위치를 통째로 튜플에 저장 -> bfs를 돌면서 현재위치와 다음위치가 일치하면 그쪽으로 안감
# bfs 큐에 들어가는 조건 : 한번도 못 만난 cow일 경우
# bfs가 끝날때 마다 distant + 1
from collections import deque
import sys
sys.stdin = open('input.txt')

#     상 우 하 좌
dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

N, K, R = map(int, input().split())

fence = []
for i in range(R):
    fence.append(tuple(map(int, input().split())))

distant = 0
visited = []
for i in range(K):
    r, c = map(int, input().split())
    Q = deque()
    if (r, c) not in visited:
        Q.append((r, c))

        while Q:
            r, c = Q.popleft()

            if (r, c) not in visited:
                visited.append((r, c))
                for j in range(4):
                    nr, nc = r + dr[j], c + dc[j]
                    if 0 < nr <= N and 0 < nc <= N:
                        if (r, c, nr, nc) not in fence and (nr, nc, r, c) not in fence:
                            Q.append((nr, nc))
        distant += 1

print(distant)
t = set()
t.update([(1, 2)])
print(t)
