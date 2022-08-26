# seniority 기록 후 arrival 순서대로 정렬 및 deque에 삽입

# time 으로 시간 관리, max_wait 으로 최대 대기시간 관리
# HeapQ 생성 후, time에 맞는 순서가 오면 deque에서 빼옴
# 파이썬의 heapq는 기본적으로 최소힙인것 참고

# heapq에서 하나씩 빼며 for loop 돌리며 time +1

# cnt는 만약 heapq에 사람이 있으면 남은시간을 저장
# heapq에 또 사람이 들어오면 cnt = cnt + 방금 들어온 사람의 먹는시간 이런식으로 갱신

from collections import deque
import sys
sys.stdin = open('input.txt')

N = int(input())

Q = []
for s in range(1, N+1):
    cow = list(map(int, input().split())) + [s]
    Q.append(cow)

Q = deque(sorted(Q, key=lambda x:x[0]))
print(Q)

line = deque(Q.popleft())
time, max_wait = 0, 0
while Q or line:
    arrival, session, seniority = line.popleft()

    if time < arrival:
        for t in range(arrival):
            time += 1

            while Q and Q[0][0] == time:
                line.append(Q.popleft())

            if time == arrival:
                break

    for t in range(session):
        time += 1
        temp = []
        while Q and Q[0][0] == time:
            temp.append(Q.popleft())
        if temp:
            temp = sorted(temp, key=lambda x:x[2])
            line += deque(temp)

    # 걸리는 시간을 어떻게 관리하면 좋을지 고민중