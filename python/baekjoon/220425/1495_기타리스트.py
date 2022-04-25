import sys
sys.stdin = open('input.txt')

# 4% 에서 메모리 초과. 역시 무조건 dp 쓰라고 만든 문제임
# 반례는 대부분 통과함

from collections import deque
# 0 <= V <= M
N, S, M = map(int, input().split())     # 곡 개수, 시작 볼륨, 최대 허용 볼륨
V = list(map(int, input().split()))
q = deque()
q.append([S, 0])
ans = -1
while q:
    cur = q.popleft()
    i = cur[1]
    if i == N:
        ans = max(ans, cur[0])
    if i < N:
        if 0 <= cur[0] + V[i] <= M:
            q.append([cur[0]+V[i], i+1])
        if 0 <= cur[0] - V[i] <= M:
            q.append([cur[0]-V[i], i+1])

print(ans)

