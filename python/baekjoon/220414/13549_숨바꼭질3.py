# 가장 빠른 시간 내에 도착하는 방법
# dfs
# 현재점 : N   /   목표점 : K
# 1초에 +1, -1    /   0초에 *2
from collections import deque
import sys
sys.stdin = open('input.txt')

# 3차 시도 멸망
N, K = map(int, input().split())
visited = [0] * 100001
dist = [-1] * 100001

q = deque()
q.append(N)   # 시작점 큐에 삽입
visited[N] = 1  # 시작점 방문 체크
dist[N] = 0     # 이동한 거리 표시

# 44% 에서 실패
# 해결 : 26번 줄 참고
# 질문1 : 반례가 뭘까
# big O 표기법 시간
#    - 참고 : https://blog.yevgnenll.me/posts/calculate-recursive-big-o-number-of-steps-to-reduce-a-number-to-zero
while q:
    cur = q.popleft()
    # 순간이동을 제일 먼저 고려를 해줘야 이동 거리 줄일 수 있음, 고로 appendleft()활용해서 우선순위 조정.
    if cur*2 < 100001 and not visited[cur*2]:  # 해당 위치로 순간이동 가능하면
        q.appendleft(cur*2)
        visited[cur*2] = 1
        dist[cur*2] = dist[cur]                 # 순간이동은 이동거리 +0
    if cur + 1 < 100001 and not visited[cur+1]:     # 해당 위치로 +1 걸어갈수 있으면
        q.append(cur+1)
        visited[cur+1] = 1
        dist[cur+1] = dist[cur] + 1             # 걸으면 이동거리 +1
    if cur - 1 >= 0 and not visited[cur-1]:     # # 해당 위치로 -1 걸어갈수 있으면
        q.append(cur-1)
        visited[cur-1] = 1
        dist[cur-1] = dist[cur] + 1             # 걸으면 이동거리 +1
    # if dist[K] == K:
    #     break

print(dist[K])


# 2차시도 실패
# 이동한 누적 횟수를 아예 기록 안함
# N, K = map(int, input().split())
# visited = [0] * 100001
#
# q = deque()
# q.append(N)   # 시작점 큐에 삽입
#
# while q:
#     cur = q.popleft()
#     if cur*2 < 100001 and not visited[cur*2] and visited[cur]:  # 해당 위치로 순간이동 가능하면
#         q.append(cur*2)
#         visited[cur*2] = cur * 2
#     if cur + 1 < 100001 and not visited[cur+1]:
#         q.append(cur+1)
#         visited[cur+1] = cur + 1
#     if cur - 1 >= 0 and not visited[cur-1]:
#         q.append(cur-1)
#         visited[cur-1] = cur + 1
#     if visited[K] == K:
#         break
#
# print(visited[K])



# 1시도 어림도 없는 dfs 실패
# N, K = map(int, input().split())
# visited = [0] * 100001
# ans = 999999999
#
# def dfs(n, cnt):
#     global ans
#     if n == K:
#         ans = min(ans, cnt)
#         return
#     else:
#         temp = [n-1, n+1, n*2]
#         for i in range(3):
#             if not visited[temp[i]]:
#                 visited[temp[i]] = 1
#                 if i == 2:
#                     dfs(temp[i], cnt)
#                 else:
#                     dfs(temp[i], cnt+1)
#
# dfs(N, 0)
#
# print(ans)