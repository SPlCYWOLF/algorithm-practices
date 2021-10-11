import sys
sys.stdin = open('input.txt')

'''
총 소요 시간: 55분
디버깅 시간: 35분
구현 시간: 11분
thought process: 9분 45초
dfs로 모든 인접 쓰레기들을 돌아가며 카운트 후, 가장 큰 카운트를 ans에 갱신
한번 왔던 위치는 visited처리하여 중복 방문 방지
'''
#     상 우 하 좌
dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

def dfs(r, c):
    global ans
    global cnt
    if ans < cnt:
        ans = cnt

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N+1 and 0 <= nc < M+1 and arr[nr][nc] and not visited[nr][nc]:
            visited[nr][nc] = 1
            cnt += 1
            dfs(nr, nc)


N, M, K = map(int, input().split())
visited = [[0] * (M+1) for _ in range(N+1)]
arr = [[0] * (M+1) for _ in range(N+1)]
ans = 0
for i in range(K):
    leftovers = tuple(map(int, input().split()))
    arr[leftovers[0]][leftovers[1]] = 1

for j in range(1, N+1):
    for k in range(1, M+1):
        if arr[j][k] and not visited[j][k]:
            visited[j][k] = 1
            cnt = 1
            dfs(j, k)  # 탐색 시작 위치 r and c
            cnt = 0
print(ans)