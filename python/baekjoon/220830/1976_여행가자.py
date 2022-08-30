# bfs로 모든 이동 가능 경로를 dictionary에 노드별로 저장
# 나중에 이동 가능 여부 dictionary 기반으로 판단

from collections import deque
import sys
sys.stdin = open('input.txt')

def bfs(n):         # 각 도시마다 연결되는 도시 기록
    global city_map
    current_city = n + 1
    Q = deque()
    Q.append(n)
    while Q:
        next_city = Q.popleft()
        for c in range(N):
            if c+1 not in city_map[current_city] and connections[next_city][c]:
                city_map[current_city].add(c+1)
                Q.append(c)


N = int(input())
M = int(input())
connections = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(int, input().split()))
answer_found = False
for i in range(len(plan)):      # 만약 도시 이동 계획이 없다면,
    if plan[i] != plan[0]:
        break
    if i == len(plan)-1:
        answer_found = True     # 무조건 TRUE가 정답

answer = "YES"                  # 정답 초기화
if not answer_found:            # 도시 이동 계획이 있는 경우에만 시작
    city_map = dict()
    for i in range(1, N+1):     # 도시 : set(이동 가능한 도시)
        city_map[i] = set()

    for i in range(N):          # 각 도시마다 연결되는 도시 기록
        bfs(i)

    for i in range(len(plan)-1):            # 플랜대로 이동 가능한지 여부 확인
        departure, goal = plan[i], plan[i+1]
        if goal not in city_map[departure]: # 하나라도 이동 불가능하면 정답 : NO
            answer = "NO"
            break

print(answer)