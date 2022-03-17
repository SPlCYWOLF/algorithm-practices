import sys
sys.stdin = open('input.txt')

dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

def dfs(r, c, cur, cat, sho):
    global ans

    if len(sho) == total_num:
        ans = min(ans, cur)
        return

    if cur >= ans:
        return

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]

        if 0 <= nr < N and 0 <= nc < N:
            if not visited[nr][nc]:
                if stage[nr][nc] > 0 and stage[nr][nc] in cat:  # 집 발견하고 몬스터 있는 경우
                    visited[nr][nc] = 1
                    dfs(nr, nc, cur + (abs(nr-r) + abs(nc-c)), cat, sho+[stage[nr][nc]])
                    visited[nr][nc] = 0
                elif stage[nr][nc] < 0:                         # 몬스터 발견한 경우
                    visited[nr][nc] = 1
                    dfs(nr, nc, cur + (abs(nr-r) + abs(nc-c)), cat+[abs(stage[nr][nc])], sho)
                    visited[nr][nc] = 0
                else:                                           # 몬스터 없이 집 발견하거나 아무것도 없는경우
                    dfs(nr, nc, cur, cat, sho)

# 아이디어1: 패작
# 1. 시작 위치 기록
# 2. 우하좌상 순으로 몬스터 있는지 확인
#   - 2-1 있으면 몬스터로 이동 후 시작지점부터 현재 지점까지 이동 거리 저장
#           - 1~2번 반복
#   - 2-2 없으면 우하좌상 순으로 이동
# 3. 집 발견 하면 현재 괴물 의뢰인인지 확인
#   - 3-1 해당 의뢰인이면 이동
#   - 3-2 아니면 무시
# 4. 집 & 괴물 동시 발견 시
#   - 4-1 해당 의뢰인인 경우, 집으로 이동한 경우 탐색
#   - 4-2 해당 의뢰인이 아닌 경우, 집으로 이동은 무시
#   - 4-3 괴물로 이동 경우도 탐색
# 5. 괴물들 발견하면 괴물 리스트에 체크 + 집에 돌려놓으면 체크
# 6. 다 돌려놓으면 ans에 이동 거리 기록
# 7. 추후 이동거리가 ans보다 커지면 바로 종료하고 다음걸로 넘어감
T = int(input())
for tc in range(T):
    N = int(input())
    stage = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    total_num = 0
    ans = 99

    for i in range(N):                  # 총 괴물 숫자 찾기
        for j in range(N):
            if stage[i][j] < 0:
                total_num += 1

    for i in range(N):
        for j in range(N):
            catch, shown = [], []
            current_location = 0
            dfs(i, j, current_location, catch, shown,)

print(ans)


# 방법 2
# 전체 맵 탐색 후 괴물과 의뢰인 위치정보 queue에 저장
# dfs 로 모든 괴물과 의뢰인 위치를 오가면서 축적된 이동거리를 도출
# 해당 이동거리를 ans에 저장
# 초기 ans값은 99 (N 이 최대 10이므로)
# 기존의 ans보다 이동거리 값이 커지면 바로 가지치기
# 최종 ans값이 정답.