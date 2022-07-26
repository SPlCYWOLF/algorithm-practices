# bfs 돌고
# 1개 이상 만났으면 ans += ( (전체 소) - (자신 + 만난 소) = cnt * (전체 소 - cnt) )
# 1개도 안 만났으면 single += 1    이후 bfs 다 끝나면   ans += (single 개수만큼 모드 연결 되는 노드 개수)

from collections import deque
import sys
sys.stdin = open('input.txt')


def bfs(r, c, met):
    global counted
    Q = deque()
    Q.append((r, c))

    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if not visited[nr][nc] and (r, c, nr, nc) not in fence and (nr, nc, r, c) not in fence:
                visited[nr][nc] = 1
                Q.append((nr, nc))
                if (nr, nc) in cows:
                    met += 1

    count = met * (K - met - counted)
    counted += met
    return count

#     상 우 하 좌
dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

N, K, R = map(int, input().split())
fence = tuple(tuple(map(int, input().split())) for _ in range(R))
visited = [[1] * (N+2)] + [[1] + [0] * N + [1] for _ in range(N)] + [[1] * (N+2)]
cows = tuple(tuple(map(int, input().split())) for _ in range(K))

ans = 0
counted = 0
for i in range(K):
    r, c = cows[i]
    met = 1
    if not visited[r][c]:
        visited[r][c] = 1
        ans += bfs(r, c, met)

print(ans)





# def bfs(r, c, met):
#     global single, counted
#     Q = deque()
#     Q.append((r, c))
#
#     while Q:
#         r, c = Q.popleft()
#         for i in range(4):
#             nr, nc = r + dr[i], c + dc[i]
#             if not visited[nr][nc] and (r, c, nr, nc) not in fence and (nr, nc, r, c) not in fence:
#                 visited[nr][nc] = 1
#                 Q.append((nr, nc))
#                 if (nr, nc) in cows:
#                     met += 1
#     if met > 1:
#         count = met * (K - met - counted)
#         counted += met
#         return count
#     else:
#         single += 1
#         return 0
#
#
# #     상 우 하 좌
# dr = (-1, 0, 1, 0)
# dc = (0, 1, 0, -1)
#
# N, K, R = map(int, input().split())
# fence = tuple(tuple(map(int, input().split())) for _ in range(R))
# visited = [[1] * (N+2)] + [[1] + [0] * N + [1] for _ in range(N)] + [[1] * (N+2)]
# print(fence)
# print(visited)
# cows = tuple(tuple(map(int, input().split())) for _ in range(K))
#
# ans = 0
# single = 0
# counted = 0
# for i in range(K):
#     r, c = cows[i]
#     met = 1
#     if not visited[r][c]:
#         visited[r][c] = 1
#         ans += bfs(r, c, met)
#
# j, comb = 1, 0
# while single > j:
#     comb = j + comb
#     j += 1
#
# print(ans + comb)





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