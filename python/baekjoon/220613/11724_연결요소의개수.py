import sys
sys.stdin = open('input.txt')

# dfs로 돌아서 연결된 정점 확인
# 방문 노드는 visit 처리하여 중복 방문 방지
# 방문 끝나면 cnt + 1
# 주어진 간선의 개수만큼 input을 받으면, cnt 출력 후 종료

def dfs(n):
    visited[n] = 1
    for k in range(n):
        if not visited[k]:
            dfs(k)


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 0

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
print(graph)

for j in range(1, N+1):
    if not visited[j]:
        if graph[j]:
            dfs(j)
            cnt += 1
print(cnt)
