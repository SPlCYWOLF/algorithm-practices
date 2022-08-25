import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt')

# 성공
# 패작 4 와 동일하지만,
# 각 dfs의 길 탐색 용 => visited
# 물이 새는 길 기록용 => flood
# 이미 ans에 축적된 위치 기록용 count로
# 정보 관리를 하였다.

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

def seperate(nums):
    temp = [*nums]
    return map(int, temp)

def dfs(h, r, c):
    global escape, cnt

    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]

        if escape:
            counted[r][c] = 0
            flood[r][c] = 1
            flood[nr][nc] = 1
            return

        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            if nr == 0 or nr == N - 1 or nc == 0 or nc == M - 1:
                if field[nr][nc] < h:
                    escape = True
                    flood[nr][nc] = 1
                    cnt = 0
                    return

            if field[nr][nc] < h:
                visited[nr][nc] = 1
                counted[nr][nc] = 1
                cnt += 1
                dfs(h, nr, nc)
                if escape:
                    counted[nr][nc] = 0
                    flood[nr][nc] = 1
                    return


N, M = map(int, input().split())
field = [tuple(seperate(input())) for _ in range(N)]
print(field)

highest = 0
for i in range(N):
    highest = max(max(field[i]), highest)

ans = 0

coordinates = []
for h in range(highest, 0, -1):
    for i in range(1, N-1):
        for j in range(1, M-1):
            if field[i][j] < h:
                coordinates.append((h, i, j))

visited = [[0] * M for _ in range(N)]
flood = [[0] * M for _ in range(N)]
counted = [[0] * M for _ in range(N)]
temp = highest
for c in coordinates:
    h, r, c = c
    escape, cnt = False, 0
    visited = [[0] * M for _ in range(N)]

    if temp != h:
        temp = h
        flood = [[0] * M for _ in range(N)]     #
        counted = [[0] * M for _ in range(N)]

    if not flood[r][c] and not counted[r][c]:
        cnt += 1
        counted[r][c] = 1
        visited[r][c] = 1
        dfs(h, r, c)

    ans += cnt

print(ans)








# 패작 4 : 스파게티코드로 멘붕
# BFS가 아닌, DFS로 풀이 시도
# visit 관리를 해당 높이의 글로벌 visit과, 해당 dfs스코프의 visit으로 따로 관리
# 나머지 로직은 패작2 와 동일함

# dr = (-1, 0, 1, 0)
# dc = (0, 1, 0, -1)
#
# def seperate(nums):
#     temp = [*nums]
#     return map(int, temp)
#
# def dfs(h, r, c):
#     global stop, cnt, local_visited
#
#     for k in range(4):
#
#         if stop:
#             local_visited[r][c][1] = 4
#             return
#
#         nr, nc = r + dr[k], c + dc[k]
#
#         if visited[nr][nc][1] == 4 or local_visited[nr][nc][1] == 4:
#             stop = True
#             local_visited[nr][nc][1] = 4
#             cnt = 0
#             return
#
#         if 0 <= nr < N and 0 <= nc < M and not local_visited[nr][nc][0]:
#
#             if nr == 0 or nr == N-1 or nc == 0 or nc == M-1:
#                 if field[nr][nc] < h:
#                     # 만약 테두리에 물이 새면 무조건 물 다 빠지니 해당 bfs 탐색 종료
#                     stop = True
#                     local_visited[nr][nc][1] = 4
#                     cnt = 0
#                     return
#
#             # 벽이 아니면 dfs 진행
#             if field[nr][nc] < h:
#                 local_visited[nr][nc][0] = 1
#                 cnt += 1
#                 dfs(h, nr, nc)
#
#
# N, M = map(int, input().split())
# field = [tuple(seperate(input())) for _ in range(N)]
# highest = 0
# for i in range(N):
#     highest = max(max(field[i]), highest)
#
# ans = 0
#
# coordinates = []
# for h in range(highest, 0, -1):
#     for i in range(1, N-1):
#         for j in range(1, M-1):
#             if field[i][j] < h:
#                 coordinates.append((h, i, j))
#
# visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
# local_visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
# temp = highest
#
# for c in coordinates:
#     stop, cnt = False, 0
#     h, r, c = c
#
#     if temp != h:
#         visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
#         local_visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
#         temp = h
#
#     if not visited[r][c][0] and not local_visited[r][c][0]:
#         cnt += 1
#         local_visited[r][c][0] = 1
#         dfs(h, r, c)
#         visited = local_visited
#         # visited 안했으면, 해당 위치에서 bfs 시작
#         # 벽을 만나면 Q 안넣음
#
#     ans += cnt
#
# print(ans)






# 패작 3 : 반례는 다 통과함, 원인 불명;
#
# dr = (-1, 0, 1, 0)
# dc = (0, 1, 0, -1)
#
# def seperate(nums):
#     temp = [*nums]
#     return map(int, temp)
#
# def bfs(h, r, c, visited):
#     test_visited, cnt = [], 1
#     test_visited.append((r, c))
#     Q = deque()
#     Q.append((r, c))
#     while Q:
#         r, c = Q.popleft()
#
#         for k in range(4):
#             nr, nc = r + dr[k], c + dc[k]
#
#             if 0 <= nr < N and 0 <= nc < M and (nr, nc) not in test_visited:
#
#                 if nr == 0 or nr == N-1 or nc == 0 or nc == M-1:
#                     if field[nr][nc] < h:
#                         # 만약 테두리에 물이 새면 무조건 물 다 빠지니 bfs자체를 종료
#                         return 0
#
#                 # 벽이 아니면 bfs 진행
#                 if field[nr][nc] < h:
#                     test_visited.append((nr, nc))
#                     Q.append((nr, nc))
#                     cnt += 1
#                     continue
#
#     for coordinates in test_visited:
#         x, y = coordinates
#         visited[x][y] = 1
#
#     return cnt      # 끝까지 bfs 돌면, cnt 개수
#
#
# N, M = map(int, input().split())
# field = [tuple(seperate(input())) for _ in range(N)]
#
# highest = max(max(field))
# ans = 0
#
# coordinates = []
# for h in range(highest, 0, -1):
#     for i in range(1, N-1):
#         for j in range(1, M-1):
#             coordinates.append((h, i, j))
#
# visited = [[0] * M for _ in range(N)]
# temp = highest
# for c in coordinates:
#     h, r, c = c
#
#     if temp != h:
#         visited = [[0] * M for _ in range(N)]
#
#     temp = h
#     if field[r][c] < h and not visited[r][c]:
#         ans += bfs(h, r, c, visited)
#         # visited 안했으면, 해당 위치에서 bfs 시작
#         # 벽을 만나면 Q 안넣음
# print(ans)





# 패작 2 :
# 3차원 배열을 돌며 맨 위에서부터 한칸씩 내려오며 물 채움
# 남기는 조건 : 4방향 다 벽이 있어야함
# 채워지면 cnt + 1
# 맨 아래 도달할때 까지 반복

# from collections import deque
# import sys
# sys.stdin = open('input.txt')
#
# dr = (-1, 0, 1, 0)
# dc = (0, 1, 0, -1)
#
# def seperate(nums):
#     temp = [*nums]
#     return map(int, temp)
#
# def bfs(h, r, c, visited):
#     test_visited, cnt = [], 1
#     test_visited.append((r, c))
#     Q = deque()
#     Q.append((r, c))
#     while Q:
#         r, c = Q.popleft()
#
#         for k in range(4):
#             nr, nc = r + dr[k], c + dc[k]
#
#             if 0 <= nr < N and 0 <= nc < M and (nr, nc) not in test_visited:
#
#                 if nr == 0 or nr == N-1 or nc == 0 or nc == M-1:
#                     if field[nr][nc] < h:
#                         # 만약 테두리에 물이 새면 무조건 물 다 빠지니 bfs자체를 종료
#                         return 0
#
#                 # 벽이 아니면 bfs 진행
#                 if field[nr][nc] < h:
#                     test_visited.append((nr, nc))
#                     Q.append((nr, nc))
#                     cnt += 1
#                     continue
#
#     for coordinates in test_visited:
#         x, y = coordinates
#         visited[x][y] = 1
#
#     return cnt      # 끝까지 bfs 돌면, cnt 개수
#
#
# N, M = map(int, input().split())
# field = [tuple(seperate(input())) for _ in range(N)]
#
# highest = max(max(field))
# ans = 0
#
# for h in range(highest, 0, -1):
#     visited = [[0] * M for _ in range(N)]
#
#     for r in range(1, N-1):
#
#         for c in range(1, M-1):
#             if field[r][c] < h and not visited[r][c]:
#                 ans += bfs(h, r, c, visited)
#                 # visited 안했으면, 해당 위치에서 bfs 시작
#                 # 벽을 만나면 Q 안넣음
# print(ans)





# 패작 1

# 테두리 칸 제외, 모든 칸 돌며 각 칸마다 bfs 시작

# 매 bfs 마다 상 우 하 좌 순으로 본인보다 크지만 가장 낮은 벽 높이 저장하며 진행
# 상하좌우 확인하며 본인과 같거나 작고,
# visited 아니면, 여기서 visit체크 후 높이 매게변수 리스트에 저장하며 bfs 진행

# but! 이미 visited 체크 되어있으면, test_visit 체크하고 bfs들어가고 높이는 저장 안함
# 그리고 bfs 시작점과 nr nc 를 비교해서 bfs 진입 여부 결정
# 그리고 매게변수 리스트에 본인 저장

# 만약 test_visit도 체크되어있으면 bfs 안들어감
# 본인 높이보다 높으면 bfs 안 들어감

# 마지막에 상하좌우에서 가장 작은 벽 높이 - 각 저장된 매게변수 리스트의 각 높이 의 총 값 ans에 축적
# 무사히 bfs 다 돌았으면, test_visit도 visited에 반영해준다

# bfs돌다가 한 곳이라도 테두리 값이 본인거보다 작으면, 종료 (물 다샘)

# 새로운 bfs들어갈때는 visited

# 반복
#
# from collections import deque
# import sys
# sys.stdin =open('input.txt')
#
# # 상 우 하 좌
# dr = (-1, 0, 1, 0)
# dc = (0, 1, 0, -1)
#
# def seperate(nums):
#     temp = [*nums]
#     return map(int, temp)
#
# def bfs(r, c):
#     OR, OC = r, c
#     heights, min_wall = [field[r][c]], 9999999999
#     test_visited = [[r, c]]
#     Q = deque()
#     Q.append([r, c])
#     while Q:
#         r, c = Q.popleft()
#         for k in range(4):
#             nr, nc = r + dr[k], c + dc[k]
#
#             if visited[nr][nc] and field[OR][OC] > field[nr][nc]:
#                 if [nr, nc] not in test_visited:
#                     test_visited.append([nr, nc])
#                     Q.append([nr, nc])
#                 continue
#
#             if [nr, nc] not in test_visited and field[r][c] < field[nr][nc]:
#                 min_wall = min(min_wall, field[nr][nc])
#                 continue
#
#             if nr == 0 or nr == N-1 or nc == 0 or nc == M-1:
#                 return 0
#
#             if field[r][c] >= field[nr][nc]:
#                 if [nr, nc] not in test_visited:
#                     test_visited.append([nr, nc])
#                     Q.append([nr, nc])
#                     if not visited[nr][nc]:
#                         heights.append(field[nr][nc])
#                 continue
#
#     if min_wall <= field[OR][OC]:
#         return 0
#
#     for v in test_visited:
#         r, c = v
#         visited[r][c] = 1
#
#     temp = 0
#     for h in heights:
#         temp += min_wall - h
#
#     return temp
#
#
# N, M = map(int, input().split())
# field = [tuple(seperate(input())) for _ in range(N)]
# visited = [[0] * M for _ in range(N)]
#
# print(field)
# ans = 0
# for i in range(1, N-1):
#     for j in range(1, M-1):
#         if not visited[i][j]:
#             ans += bfs(i, j)
#
# print(ans)