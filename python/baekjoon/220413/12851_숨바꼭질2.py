# 수빈이 현재 위치 : N
# 동생 현재 위치 : K
# 걸으면 +1 or -1    순간이동하면 *2
# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간
# 그리고 가장 빠른 시간으로 찾는 방법이 몇가지인지 구하라      bfs


# 40분 소요
# https://glowdev.tistory.com/70 출처 이해 불가

from collections import deque
import sys
sys.stdin = open('input.txt')


N, K = map(int, input().split())
visited = [0] * 100001
visited[N] = 1
dist = [-1] * 100001
q = deque()
dist[N] = 0
q.append(N)

cnt = 0
min_num = 100000
ans = deque()
while q:
    cur = q.popleft()
    if dist[K] < 0:
        if cur+1 < 100001 and not visited[cur+1]:
            visited[cur+1] += 1
            dist[cur+1] = dist[cur] + 1
            q.append(cur+1)
        if cur-1 >= 0 and not visited[cur-1]:
            visited[cur-1] += 1
            dist[cur-1] = dist[cur] + 1
            q.append(cur-1)
        if cur*2 < 100001 and not visited[cur*2]:
            visited[cur*2] += 1
            dist[cur*2] = dist[cur] + 1
            q.append(cur*2)
    if cur+1 == K or cur-1 == K or cur*2 == K:
        cnt += 1


print(dist)
print(visited)
# while q:
#     cur = q.popleft()
#     if dist[K] < 0:
#         if cur+1 < 100001:
#             visited[cur+1] = 1
#             dist[cur+1] = dist[cur] + 1
#             q.append(cur+1)
#         if cur-1 >= 0:
#             visited[cur-1] = 1
#             dist[cur-1] = dist[cur] + 1
#             q.append(cur-1)
#         if cur*2 < 100001:
#             visited[cur*2] = 1
#             dist[cur*2] = dist[cur] + 1
#             q.append(cur*2)
#     if cur+1 == K or cur-1 == K or cur*2 == K:
#         cnt += 1
print()
print(dist[K])
print(cnt)
