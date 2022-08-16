# 치즈의 위치를 모두 저장
# 각 치즈의 위치에서 4번 빈 공간인지 확인 후 2개 이상 빈 공기에 노출되어 있으면 삭제 큐에 넣음
# 모든 치즈 확인 하면 삭제 큐 돌면서 치즈 모양 갱신
# 시간 카운트 +1
# 처음 받았던 치즈 리스트가 빌때 까지 반복

# 실패1 : "외부 공간"을 판단할 로직 필요
#         외부공간을 3으로 정하고, 처음 bfs통해서 기록
#         매번 치즈 삭제가 진행 되고 외부공간 정보도 갱신하는데, visited 활용해서
#         bfs를 최소화 시키기

from collections import deque
import sys
sys.stdin = open('input.txt')


dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

def markOutside():

    candidates = deque()
    found = 0
    for i in range(N):
        if found:
            break
        for j in range(M):
            if cheeze_map[i][j] == 0:
                candidates.append([i, j])
                found = 1
                break

    while candidates:
        r, c = candidates.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and cheeze_map[nr][nc] == 0:
                cheeze_map[nr][nc] = 3
                visited[nr][nc] = 1
                candidates.append([nr, nc])



def willMelt(r, c):
    cnt = 0
    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]

        if 0 <= nr < N and 0 <= nc < M and cheeze_map[nr][nc] == 3:
            cnt += 1

    if cnt >= 2:
        return True
    else:
        return False


N, M = map(int, input().split())
cheeze_map = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
markOutside()

cheeze = []
for i in range(N):
    for j in range(M):
        if cheeze_map[i][j]:
            cheeze.append([i, j])

time = 0
while cheeze:
    del_Q = []
    for c in cheeze:
        r, c = c
        if willMelt(r, c):
            del_Q.append([r, c])

    for d in del_Q:
        r, c = d
        cheeze.remove(d)
        cheeze_map[r][c] = 3

    markOutside()

    time += 1

print(time)