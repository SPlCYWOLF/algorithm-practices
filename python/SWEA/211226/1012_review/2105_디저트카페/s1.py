'''
미 완료
디버깅 시간 : 2시간
풀이시간: 1시간 34분
thought process: 9분 10초

시작점을 기점으로 dfs활용하는-데
원소값들의 순서는 상관없고 총 합만 상관있으니, combination 활용??.
그냥 맨 윙에 양 끝 원소들 빼고 중간 원소들만 순회해도 되네

대각선 방향 델타 값 활용하여 경로를 순회
무조건 사각형 모양을 그려야한다! (인자값 넘겨줘서 방향델타값 keep track)
순회하며 카운트 중첩
오직 시작 위치로 돌아왔을시 카운트 인정 + 최대값이면 업데이트.

강제 종료 조건:
1. 한번 방문했던 원소값을 방문
2. 이미 방문했던 인덱스 위치를 방문
3. 모서리 인덱스 위치 방문


구현에있어 문제점:
1. 매번 탐색마다 방향전환을 4번으로 제한 기능 구현 dunno how why
    ANSWER => 해당 원소에 방문하기전에 미리 가능여부 판단하여 방문여부 결정으로 해결

2. 첫번째 dfs 가 끝나고, 다음 for loop 타지 못하고 tuple index out of range 오류메세지
    ANSWER => 인자로 넘기는 direction 인덱스 관리

'''


import sys
sys.stdin = open('input.txt')

#   우하 좌하 좌상 우상
dr = (1, 1, -1, -1)
dc = (1, -1, -1, 1)

def dfs(r, c, direction, check, cnt):
    global ans

    if direction < 4:
        nr = r + dr[direction]
        nc = c + dc[direction]
    else:
        return

    if 0 <= nr < N and 0 <= nc < N:       # road 범위 안에 있고, 방향전환 횟수가 남아있으면 진행

        if nr == start_row and nc == start_col and cnt >= 3:        # 사각형을 그리며 첫 방문했던 위치 돌아오고
            if ans < cnt:                                           # 최대값 이라면,
                ans = cnt                                           # cnt 값 ans 에 반영
            return

        if road[nr][nc] not in check:                       # 중복되는 원소가 없다면
            dfs(nr, nc, direction, check + [road[nr][nc]], cnt + 1)          # 현재요소에서 방향전환 안하고 확인 마친 원소로 이동

    dfs(r, c, direction + 1, check, cnt)                        # 현재요소에서 전진하지않고 방향만 전환
    return

for tc in range(1, int(input())+1):
    N = int(input())
    road = tuple(tuple(map(int, input().split())) for _ in range(N))
    ans = -1
    for i in range(0, N-2):
        for j in range(1, N-1):

            start_row, start_col = i, j
            if road[start_row][start_col] != road[start_row+1][start_col+1]:    # 첫 이동 위치의 원소가 다를 경우만 실행
                tmp = []
                dfs(i, j, 0, tmp + [road[start_row][start_col]], 1)             # r, c, 방향 델타 값 인덱스, 이동시 중복 원소값 확인용 리스트, 방문횟수

    print('#{} {}'.format(tc, ans))