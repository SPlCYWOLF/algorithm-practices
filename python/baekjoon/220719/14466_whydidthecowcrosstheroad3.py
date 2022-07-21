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

cows = []
for i in range(K):
    cows.append(tuple(map(int, input().split())))

visited = []
distant = set()
for i in range(K):
    r, c = cows[i]
    Q = deque()
    temp = cows[::]
    temp.remove((r, c))
    print(f'starting cow: {r, c}')
    if (r, c) not in visited:
        Q.append((r, c))

        while Q:
            r, c = Q.popleft()

            for j in range(4):
                nr, nc = r + dr[j], c + dc[j]

                if 0 < nr <= N and 0 < nc <= N and (nr, nc) not in visited:
                    if (r, c, nr, nc) not in fence and (nr, nc, r, c) not in fence:
                        visited.append((nr, nc))
                        print(f'visits : {(nr, nc)} / currently not accessed cows : {temp}')
                        if (nr, nc) in temp:
                            temp.remove((nr, nc))
                        Q.append((nr, nc))

        print(f'not accessible cows : {temp}')
        for distant_cow in temp:
            x, y = distant_cow
            distant.update([(x, y, cows[i][0], cows[i][1]), (cows[i][0], cows[i][1], x, y)])
        print(f'distant cows : {distant}')
        print()
print(len(distant) // 2)
# t = set()
# t.update([(1, 2)])
# print(t)
