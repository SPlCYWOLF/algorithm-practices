import sys
sys.stdin = open('input.txt')

# 좌 우 상 하
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# 1. 현재 위치를 들고다니지 않을때
# r,c = 좌표, road=지금까지 조성된 등산로길이, skill=공사 유무여부
def work(r, c, road, skill):

    global ans
    if road > ans:
        ans = road

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < N and not v[nr][nc]:
            # 현 위치보다 낮은곳으로 이동 시
            if m[r][c] > m[nr][nc]:
                work(nr, nc, road+1, skill)
            # 현 위치보다 높거나 같은곳으로 이동 시
            elif skill and m[r][c] > m[nr][nc] - K:
                tmp = m[nr][nc]             # 길 깍기 전, 복구 위해 저장
                m[nr][nc] = m[r][c] - 1
                work(nr, nc, road+1, 0)     # 깍아내리기 스킬 사용
                m[nr][nc] = tmp             # 길 원상복구


# 현재위치를 들고다닐 때
def work2(r, c, h, road, skill):
    global ans
    v[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr >= N or nc < 0 or nc >= N or v[nr][nc]:
            continue
        if h > m[nr][nc]:
            work(nr, nc, road+1, skill)
        elif skill and h > m[nr][nc] - K:
            work2(nr, nc, m[r][c]-1, road+1, 0)


for tc in range(1, int(input()) + 1):

    N, K = map(int, input().split())                    # 한 변의 길이, 최대공사 가능 깊이

    m = [list(map(int, input().split())) for _ in range(N)]     # 지도
    max_h = 0                                                   # 최대높이 봉우리 저장값
    for i in range(N):
        for j in range(N):
            if max_h < m[i][j]:
                max_h = m[i][j]

    v = [[0] * N for _ in range(N)]
    ans = 0

    for i in range(N):
        for j in range(N):
            if m[i][j] == max_h:
                # work(i, j, 1, 1)    # 좌표, 길이, 길, 스킬 사용가능 횟수
                work2(i, j, max_h, 1, 1)
    print('#{} {}'.format(tc, ans))