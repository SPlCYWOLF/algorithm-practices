# 수빈이 현재 위치 : N
# 동생 현재 위치 : K
# 걸으면 +1 or -1    순간이동하면 *2
# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간
# 그리고 가장 빠른 시간으로 찾는 방법이 몇가지인지 구하라      bfs

# 2d 상에서 bfs 구현

# 40분 소요
# https://glowdev.tistory.com/70 출처 이해 불가

from collections import deque
import sys
sys.stdin = open('input.txt')


N, K = map(int, input().split())
visited = [0] * 100001
visited[N] = 1

deq = deque()
deq.append(N)

time = 0

cnt = 0

while deq:
    q = deq.popleft()

    if q == K:


    for i in q+1, q-1, q*2:
        if not time and not visited[i] and i == K:
            visited[i] = 1