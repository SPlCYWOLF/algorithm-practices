# 현재 시간 > 현재 소 도착시간:
#   대기시간 == 현재시간 현재 소의 도착시간
# 현재시간 보다 현재 소 도착시간이 늦어지면:
#   대기시간 == 0

from collections import deque
import sys
sys.stdin = open('input.txt')

N = int(input())

Q = []
for s in range(1, N+1):
    cow = list(map(int, input().split())) + [s]
    Q.append(cow)

Q = deque(sorted(Q, key=lambda x:x[0]))

line = deque([Q.popleft()])
max_wait, time = 0, 0

while Q or line:
    if line:
        arrival, session, seniority = line.popleft()
    else:
        arrival, session, seniority = Q.popleft()

    if time > arrival:                              # 현재시간 > 현재 소의 도착시간:
        max_wait = max(max_wait, time - arrival)    # 대기시간 = 현재시간 - 현재 소의 도착시간
        time += session             # 현재 시간 update
    else:                                           # 현재시간  <= 현재 소의 도착시간:
        time = arrival + session                    # 대기시간 = 0

    while Q:                            # 소가 남아있으면
        if Q[0][0] < time:              # 도착 여부 확인 후
            line.append(Q.popleft())    # 대기줄에 넣기
        else:
            break

    line = deque(sorted(line, key=lambda x: x[2]))  # 대기줄 나이순으로 정렬

print(max_wait)









# line = deque([Q.popleft()])
# time, max_wait = 0, 0
# while Q or line:
#     if line:
#         arrival, session, seniority = line.popleft()
#     else:
#         arrival, session, seniority = Q.popleft()
#
#     if time < arrival:  # 아직 도착하지 않았으면
#         for t in range(arrival):
#             if time == arrival: # 도착하면 시간 재는것 스탑
#                 break
#             time += 1           # 도착할때 까지 시간 재고
#
#     for t in range(session):    # 먹는 동안 시간 재면서
#         while Q and Q[0][0] == time:    # 먼는 도중 도착하는 소는 line에 전부 넣고
#             line.append(Q.popleft())
#         time += 1
#
#     line = deque(sorted(line, key=lambda x:x[2]))   # 새로운 line 순서 정돈
#
#     if line and arrival + session > line[-1][0]:
#         max_wait = max(max_wait, arrival + session - line[-1][0])
#
# print(max_wait)

#






# 패작 2
# 인풋값에 seniority값 할당
# 도착 했는데 이미 먹고있으면, 남은 먹는 횟수 + 내 앞에 기다리는 사람들의 먹는횟수 = 대기시간

# line 순서 정렬 할 때 마다 마지막 대기자의 대기시간 max_wait과 비교 및 갱신

# 최대 대기시간 = 정답

# from collections import deque
# import sys
# sys.stdin = open('input.txt')
#
# N = int(input())
#
# Q = []
# for s in range(1, N+1):
#     cow = list(map(int, input().split())) + [s]
#     Q.append(cow)
#
# Q = deque(sorted(Q, key=lambda x:x[0]))
#
# line = deque([Q.popleft()])
# time, max_wait = 0, 0
# while Q or line:
#     if line:
#         arrival, session, seniority = line.popleft()
#     else:
#         arrival, session, seniority = Q.popleft()
#
#     if time < arrival:  # 아직 도착하지 않았으면
#         for t in range(arrival):
#             if time == arrival: # 도착하면 시간 재는것 스탑
#                 break
#             time += 1           # 도착할때 까지 시간 재고
#
#     wait_time = 0
#     for t in range(session):    # 먹는 동안 시간 재면서
#         while Q and Q[0][0] == time:    # 먼는 도중 도착하는 소는 line에 전부 넣고
#             line.append(Q.popleft())
#
#         if line:                # 먹는동안 대기줄이 생기면, 대기 시간 축적
#             wait_time += 1
#         time += 1
#
#     line = deque(sorted(line, key=lambda x:x[2]))   # 새로운 line 순서 정돈
#
#     for w in range(len(line)-1):        # 다음으로 기다리고 있는
#         wait_time += line[w][1]
#     max_wait = max(max_wait, wait_time)
# # wait_time + 다음 주자의 먹는 시간 =
#
# print(max_wait)                 # 걸리는 시간을 어떻게 관리하면 좋을지 고민중









# 패작 1
# from collections import deque
# import sys
# sys.stdin = open('input.txt')
#
# N = int(input())
#
# Q = []
# for s in range(1, N+1):
#     cow = list(map(int, input().split())) + [s]
#     Q.append(cow)
#
# Q = deque(sorted(Q, key=lambda x:x[0]))
#
# line = deque([Q.popleft()])
# wait_record = [0] * N
# time, max_wait, i = 0, 0, 0
# while Q or line:
#     if line:
#         arrival, session, seniority = line.popleft()
#     else:
#         arrival, session, seniority = Q.popleft()
#
#     if time < arrival:  # 아직 도착하지 않았으면
#         for t in range(arrival):
#             if time == arrival: # 도착하면 시간 재는것 스탑
#                 break
#             time += 1           # 도착할때 까지 시간 재고
#
#     for t in range(session):    # 먹는 동안 시간 재면서
#         while Q and Q[0][0] == time:    # 먼는 도중 도착하는 소는 line에 전부 넣고
#             line.append(Q.popleft())
#             max_wait = max(max_wait, wait_record[i])
#             i += 1
#         if line:
#             wait_record[i] += 1
#         time += 1
#
#     line = deque(sorted(line, key=lambda x:x[2]))   # 새로운 line 순서 정돈
#
# print(wait_record)
# print(max_wait)                 # 걸리는 시간을 어떻게 관리하면 좋을지 고민중