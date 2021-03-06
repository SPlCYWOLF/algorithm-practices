import sys
sys.stdin = open('input.txt')

# 패작2
# 너무 오래걸림, 정확도 확인 필요 있음
# dfs + memoization 풀이
def dfs(cw, cv):

    if cw > K:
        return

    if memo[cw] > cv:
        return

    for j in range(N):
        if not visited[j]:
            w, v = items[j]
            memo[cw] = max(memo[cw], cv)
            visited[j] = 1
            dfs(cw+w, cv+v)
            visited[j] = 0


N, K = map(int, input().split())        # 물품개수, max무게
items = [list(map(int, input().split())) for _ in range(N)]     # 물건의무게, 물건의가치
visited = [0] * N
memo = [0] * 50

dfs(0, 0)       #현재 총 무게, 현재 총 가치
print(max(memo))





# 패작 1
# 소요시간 80분
# dfs + memoization 으로 풀이시도

# def dfs(w, v, cw, cv, item):
#     global ans
#     if cw > K:
#         return
#
#     if cw == K:
#         ans = max(ans, cv)
#         return
#
#     # if ans > cv:
#     #     return
#
#     if memo[w][item] > cv:
#         return
#
#     else:
#         for j in range(N):
#             if not visited[j]:
#                 visited[j] = 1
#                 nw, nv = items[j]
#                 if cw + nw <= K:
#                     memo[nw][j] = max(memo[nw][j] + nv, cv + nv)
#                 dfs(nw, nv, cw + nw, cv + nv, j)
#                 visited[j] = 0
#
#
# N, K = map(int, input().split())        # 물품 수, 버틸 무게
# items = [list(map(int, input().split())) for _ in range(N)]
# ans = 0
# visited = [0] * N
# memo = [[0] * (N+1) for _ in range(K+1)]
#
# for i in range(N):
#     W, V = items[i]
#     visited[i] = 1
#     if W <= K:
#         memo[W][i] = max(memo[W][i], V)
#     dfs(W, V, 0+W, 0+V, i)       # W: 무게   V: 가치   , 누적된 무게, 누적된 가치, 현재 물건
#     visited[i] = 0
#
# print(ans)
# print(memo)