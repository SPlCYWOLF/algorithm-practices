'''

thought process: 4분 15초
dfs 로 찾자.
방향 델타값 활용해서 이동방향 정하고
백트래킹으로 visited 관리하고
도착지점까지 최소 이동횟수 갱신하면서,
해당 최솟값 지나도 도착 못하면, 바로 나가리 하는 식으로 branching

'''

import sys
sys.stdin = open('input.txt')

#     상 우 하 좌
dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

def dfs(r, c, cnt):
    global ans, recur

    if cnt < ans:
        if r+1 == N and c+1 == M:
            ans = cnt
            return
        

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < M:
            if arr[nr][nc] == '1' and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                recur += 1
                dfs(nr, nc, cnt+1)
                visited[nr][nc] = 0


for tc in range(1, int(input())+1):

    N, M = map(int, input().split())
    arr = tuple(input() for _ in range(N))
    visited = [[0] * M for _ in range(N)]
    ans = 10000000000
    recur = 0
    dfs(0, 0, 1)       # 시작 위치 r & c, 그리고 이동 횟수
    print('#{} 정답: {}   재귀횟수: {}'.format(tc, ans, recur))
