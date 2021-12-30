import sys
sys.stdin = open('input.txt')

#   우하, 좌하, 좌상, 우상
dr = (1, 1, -1, -1)
dc = (1, -1, -1, 1)

# dfs 함수
def dfs(r, c, visited, cnt):
    global ans, temp
    if temp == -1:
        if cnt < 4:
            nr = r + dr[cnt]
            nc = c + dc[cnt]
        else:
            return

        if 0 <= nr < N and 0 <= nc < N:

            if cnt == 3 and len(visited) > 3 and nr == row and nc == col and arr[nr][nc] in visited:
                ans = max(ans, len(visited))
                temp = 1

            if arr[nr][nc] not in visited:
                dfs(nr, nc, visited+[arr[nr][nc]], cnt)

        dfs(r, c, visited, cnt+1)


for tc in range(1, int(input())+1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = -1
    # 1. 가로 1 ~ N-1 / 세로 0 ~ N-2 범위 내에서만 dfs 탐색 시작
    for i in range(N-2):
        for j in range(1, N-1):
            temp = -1
            row, col = i, j
            dfs(i, j, [] + [arr[i][j]], 0)   # 위치 / 방문해서 얻은 값 / 꺽긴 횟수

    print('#{} {}'.format(tc, ans))