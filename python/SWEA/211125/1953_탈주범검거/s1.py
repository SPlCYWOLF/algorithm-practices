import sys
sys.stdin = open('input.txt')
# 우 하 좌 상
dc = [0, 1, 0, -1]
dr = [1, 0, -1, 0]

pipe = [
    [0, 0, 0, 0],
    [1, 1, 1, 1],#상하좌우
    [0, 1, 0, 1],#상하
    [1, 0, 1, 0],#좌우
    [1, 0, 0, 1],#상우
    [1, 1, 0, 0],#하우
    [0, 1, 1, 0],#하좌
    [0, 0, 1, 1],#상좌
]

for tc in range(1, int(input())+1):
    N, M, R, C, L = map(int, input().split())
    # 지도정보
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    v = [[0] * M for _ in range(N)] #시간채크 겸 방문체크용

    Q = [(R, C)]
    v[R][C] = 1

    ans = 0

    while Q:
        r, c = Q.pop(0)
        ans += 1
        if v[r][c] >= L:
            continue

        # 사방향 탐색
        for d in range(4):

            curr_p = tunnel[r][c]
            # 현재 바라보는 방향으로 길이 없으면, 제외
            if pipe[curr_p][d] == 0:  # 지금 맵에서 r c 좌표의 값을 가져와서 해당 파이프에 넣고, 지금 내가 바라보고있는 방향이 0 이면, 이건 무시해도 된다라는 뜻
                continue

            nr = r + dr[d]
            nc = c + dc[d]
            # 다음 좌표가 맵을 벗어났으면, 제외
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            nd = (d + 2) % 4
            np = tunnel[nr][nc]

            # 방문을 했거나, 다음 좌표의 파이프가 현재 좌표와 연결되지 않는다면
            if v[nr][nc] or pipe[np][nd] == 0:
                continue

            v[nr][nc] = v[r][c] + 1
            Q.append((nr, nc))
    print('#{} {}'.format(tc, ans))