from collections import deque
import sys
sys.stdin = open('input.txt')

# 처음에 bfs로 치즈의 외벽 visited처리
# 2중루프 돌며 치즈이고, 해당 치즈의 2면이 외부이면 지워지는 candidate에 삽입.
# 삽입된거 나중에 한꺼번에 외벽으로 만들고, visited처리하고, 해당 지점 기준으로 bfs돌리면서
# 치즈의 새로운 외벽 visited처리 하고
# 치즈가 바닥 날 때 까지 반복

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

def updateOutside(nums):
    r, c = nums
    Q = deque()
    Q.append([r, c])

    while Q:
        r, c = Q.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]

            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if cheeze_map[nr][nc] == 0:
                    visited[nr][nc] = 1
                    Q.append([nr, nc])


def meltChecker():
    goodbye_cheeze = []
    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                continue

            if cheeze_map[i][j] == 1:
                cnt = 0
                for k in range(4):
                    nr, nc = i + dr[k], j + dc[k]
                    if cheeze_map[nr][nc] == 0 and visited[nr][nc]:
                        cnt += 1

                if cnt >= 2:
                    goodbye_cheeze.append([i, j])

    return goodbye_cheeze


def updateCheeze(nums):
    global cheeze_left
    for C in nums:
        r, c = C
        cheeze_map[r][c] = 0
        cheeze_left -= 1
        if not visited[r][c]:
            visited[r][c] = 1
            updateOutside([r, c])


N, M = map(int, input().split())
cheeze_map = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

updateOutside([0, 0])

cheeze_left = 0
for i in range(N):
    cheeze_left += cheeze_map[i].count(1)

time = 0
while cheeze_left:

    melt_cheeze = meltChecker()
    updateCheeze(melt_cheeze)

    time += 1

print(time)








# 치즈의 위치를 모두 저장
# 각 치즈의 위치에서 4번 빈 공간인지 확인 후 2개 이상 빈 공기에 노출되어 있으면 삭제 큐에 넣음
# 모든 치즈 확인 하면 삭제 큐 돌면서 치즈 모양 갱신
# 시간 카운트 +1
# 처음 받았던 치즈 리스트가 빌때 까지 반복

# 실패 : "외부 공간"을 판단할 로직 필요
#         외부공간을 3으로 정하고, 처음 bfs통해서 기록
#         매번 치즈 삭제가 진행 되고 외부공간 정보도 갱신하는데, visited 활용해서
#         bfs를 최소화 시키기

# def willMelt():
#
#     melt_candidate = []
#     for c in cheeze:
#         r, c = c
#         cnt = 0
#
#         for k in range(4):
#             nr, nc = r + dr[k], c + dc[k]
#
#             if 0 <= nr < N and 0 <= nc < M:
#                 if cheeze_map[nr][nc] == 0 and visited[nr][nc]:
#                     visited[nr][nc] = 1
#                     cnt += 1
#             if cnt >= 2:
#                 melt_candidate.append([r, c])
#                 break
#
#     return melt_candidate
#
#
# def updateCheeze(nums):
#
#     if nums:
#         for n in nums:
#             r, c = n
#             cheeze_map[r][c] = 0
#             if n in cheeze:
#                 cheeze.remove(n)
#
#     Q = deque()
#     Q.append([0, 0])
#     while Q:
#         r, c = Q.popleft()
#         for k in range(4):
#             nr, nc = r + dr[k], c + dc[k]
#
#             if 0 <= nr < N and 0 <= nc < M:
#                 if cheeze_map[nr][nc] == 0:
#                     if not visited[nr][nc]:
#                         visited[nr][nc] = 1
#                     Q.append([nr, nc])
#
#
#
# N, M = map(int, input().split())
# cheeze_map = [list(map(int, input().split())) for _ in range(N)]
# visited = [[0] * M for _ in range(N)]
#
# cheeze = []
# for i in range(N):
#     for j in range(M):
#         if cheeze_map[i][j] == 1:
#             cheeze.append([i, j])
#
# updateCheeze(0)
#
# time = 0
# while cheeze:
#
#     melt_cheeze = willMelt()
#     updateCheeze(melt_cheeze)
#
#     time += 1
#
# print(time)
# print(cheeze_map)