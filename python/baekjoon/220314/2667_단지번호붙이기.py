# 2차원 배열 숫자로 채우면서
# 방향 텔타값으로 dfs 탐색
# 한번 dfs 진입하면 끝날때가지 cnt 축적
# dfs 끝나면 바로 cnt 값 저장 후 초기화 & 단지수 +1 후 초기화


# 24분 소요
import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
house_cnt = []
danji_cnt = 0

#     상 하 좌 우
dr = (0, 1, 0, -1)
dc = (-1, 0, 1, 0)

def dfs(r, c):
    global cnt

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] and not visited[nr][nc]:
            cnt += 1
            visited[nr][nc] = 1
            dfs(nr, nc)


for i in range(N):
    for j in range(N):
        cnt = 0
        if arr[i][j] and not visited[i][j]:
            visited[i][j] = 1
            cnt += 1
            dfs(i, j)
            house_cnt.append(cnt)
            danji_cnt += 1

print(danji_cnt)
for n in sorted(house_cnt):
    print(n)