import sys
from collections import deque, defaultdict
sys.stdin = open('input.txt')

# 시간초과로 결국 통과 실패
def bfs(K, current_n):
    visited = [0] * (N+1)
    visited[current_n] = 1
    Q = deque()
    Q.append((current_n, 99999999))
    cnt = 0

    while Q:
        current_n, temp_relevance = Q.popleft()
        for goal_n, relevance in graph[current_n]:
            if relevance >= K and not visited[goal_n]:
                visited[goal_n] = 1
                cnt += 1
                Q.append((goal_n, relevance))
    return cnt


N, Q = map(int, input().split())
graph = defaultdict(list)
print(graph)

for i in range(N-1):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))
print(graph)

for i in range(Q):
    k, v = map(int, input().split())
    print(bfs(k, v))




# 주어진 가중치 그래프 생성
# 주어진 Q에 대해 bfs로 돌며 minimum 가중치와 K값을 대조하며 count 후 총 count 값을 반환

# def bfs(K, current_n):
#     visited = [0] * (N+1)
#     visited[current_n] = 1
#     Q = deque()
#     Q.append([current_n, 9999999999])
#     cnt = 0
#
#     while Q:
#         current_n, temp_relevance = Q.popleft()
#         for goal_n, relevance in graph[current_n]:
#             if not visited[goal_n]:
#                 visited[goal_n] = 1
#                 m_relevance = min(temp_relevance, relevance)
#                 if m_relevance >= K:
#                     cnt += 1
#                 Q.append([goal_n, m_relevance])
#     print(cnt)
#
#
# N, Q = map(int, input().split())
# graph = [[] for _ in range(N+1)]
#
# for i in range(N-1):
#     p, q, r = map(int, input().split())
#     graph[p] += [[q, r]]
#     graph[q] += [[p, r]]
# print(graph)
#
# for i in range(Q):
#     k, v = map(int, input().split())
#     bfs(k, v)

















# 그래프 생성
# 각 지점에서 다음 지점까지 relevence는 2차원 배열에 기록
# 한칸 넘어서 가는 지역에 대한 relevence는(2차원 배열의 빈 공간들) 두 노드가 가진 가장 작은 가중치(연관성)중에서 작은 가중치로 채워넣기
# 2차원 배열의 v인덱스를 돌며 가중치가 k값과 같거나 큰 값들의 갯수를 반환

# N, Q = map(int, input().split())
# relevance = [[0]*(N+1) for _ in range(N+1)]
# temp_relevance = [[99999]*(N+1) for _ in range(N+1)]
#
# for i in range(N-1):
#     p, q, r = map(int, input().split())
#     relevance[p][q] = r
#     relevance[q][p] = r
#     temp_relevance[p][q] = r
#     temp_relevance[q][p] = r
# pp = pprint.PrettyPrinter()
# pp.pprint(relevance)
#
# for i in range(1, N+1):
#     for j in range(1, N+1):
#         if i != j and relevance[i][j] == 0:
#             relevance[i][j] = min(min(temp_relevance[i]), min(temp_relevance[j]))
# pp.pprint(relevance)
#
# for i in range(Q):
#     k, v = map(int, input().split())
#     cnt = 0
#     for relev in relevance[v]:
#         if relev >= k:
#             cnt += 1
#     print(cnt)