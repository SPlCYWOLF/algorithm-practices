

# bfs 돌면서 조건에 부합한 경우에만 다음 경로로 이동 (노벽, 노울타리, 가본곳)
# 만나게되는

import sys
from collections import deque
sys.stdin = open('input.txt')


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(r1, c1):
    dq = deque()
    dq.append((r1, c1))
    cow_visit[r1][c1] = True
    while dq:
        x, y = dq.popleft()
        for d in range(4):
            nx = dx[d] + x
            ny = dy[d] + y
            # 범위 체크
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if cow_visit[nx][ny]:  # 방문 체크
                continue
            if (nx, ny) in road[x][y]:  # 다리인 경우 pass
                continue
            dq.append((nx, ny))
            cow_visit[nx][ny] = True

n, k, r = map(int, input().split())  # n*n, k: 마리, r: 정해진 길

road = [[[] for _ in range(n)] for _ in range(n)]
cow_visit = [[False] * n for _ in range(n)]
count = 0
# 길 위치 담기
for _ in range(r):
    r1, c1, r2, c2 = map(int, input().split())
    road[r1 - 1][c1 - 1].append((r2 - 1, c2 - 1))
    road[r2 - 1][c2 - 1].append((r1 - 1, c1 - 1))

# 소의 위치 담기
cow_list = list()
for _ in range(k):
    a, b = map(int, input().split())
    cow_list.append((a - 1, b - 1))

# 1. 소를 한마리씩 돌려가면서 방문 여부 탐색
for i, cow in enumerate(cow_list):
    cow_visit = [[False] * n for _ in range(n)]
    # 2. 현재 소가 정해진 길 없이 가는 경로를 탐색
    bfs(cow[0], cow[1])
    for r2, c2 in cow_list[i + 1:]:
        # 3. 방문을 완료하지 못한 경우 결과 + 1
        if not cow_visit[r2][c2]:
            count += 1
print(count)






# 패작1 시간초과
# bfs를 돌면서 조건에 부합한 경우에만 다음 경로로 이동(벽, 울타리, 이미 가본 곳 제외)
# bfs가 끝날때 마다 만나지 못한 cow 위치와 현재 위치를 distant에 추가 (distant 한 두 cow의 위치를 기록)
# 양뱡향으로 기록함으로써 중복 현상을 방지하고, 합산된 distant // 2 로 정답 반환
# from collections import deque
# import sys
# sys.stdin = open('input.txt')
#
# #     상 우 하 좌
# dr = (-1, 0, 1, 0)
# dc = (0, 1, 0, -1)
#
# N, K, R = map(int, input().split())
#
# fence = []
# for i in range(R):
#     fence.append(tuple(map(int, input().split())))
#
# cows = []
# for i in range(K):
#     cows.append(tuple(map(int, input().split())))
#
#
# distant = set()
# for i in range(K):
#     r, c = cows[i]
#     Q = deque()
#     temp = cows[::]
#     temp.remove((r, c))
#     print(f'starting cow: {r, c}')
#     visited = []
#     Q.append((r, c))
#
#     while Q:
#         r, c = Q.popleft()
#
#         for j in range(4):
#             nr, nc = r + dr[j], c + dc[j]
#
#             if 0 < nr <= N and 0 < nc <= N and (nr, nc) not in visited:
#                 if (r, c, nr, nc) not in fence and (nr, nc, r, c) not in fence:
#                     visited.append((nr, nc))
#                     print(f'visits : {(nr, nc)} / currently not accessed cows : {temp}')
#                     if (nr, nc) in temp:
#                         temp.remove((nr, nc))
#                     Q.append((nr, nc))
#
#     print(f'not accessible cows : {temp}')
#     for distant_cow in temp:
#         x, y = distant_cow
#         distant.update([(x, y, cows[i][0], cows[i][1]), (cows[i][0], cows[i][1], x, y)])
#     print(f'distant cows : {distant}')
#     print()
#
# print(len(distant))
# print(len(distant) // 2)