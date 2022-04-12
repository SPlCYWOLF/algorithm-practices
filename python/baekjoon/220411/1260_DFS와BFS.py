# 정점 개수 N , 간선 개수 M , 탐색을 시작할 정점의 번호 V
# 정점이 여러개면 정점 번호가 작은걸 먼저 방문
# 테스트케이스 다 정답, 하지만 백준 미통과

# 소요시간 70분
from collections import deque
import sys
sys.stdin = open('input.txt')

def dfs(v):
    if not visited[v]:
        visited[v] = 1
        ans1.append(v)
    for w in range(1, N+1):
        if G[v][w] == 1 and not visited[w]:
            dfs(w)


N, M, V = map(int, input().split())
G = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)
ans1 = []

for i in range(M):
    temp = list(map(int, input().split()))
    G[temp[0]][temp[1]] = 1 # 양방향 그래프
    G[temp[1]][temp[0]] = 1 # 양방향 그래프

dfs(V)
print(*ans1)

##################################################################

ans2 = deque()
deq = deque()
deq.append(V)

while deq:
    t = deq.popleft()
    ans2.append(t)
    for j in range(1, N+1):
        if G[t][j] == 1 and j not in ans2:
            deq.append(j)
    if len(ans2) == N:
        break

print(*ans2)