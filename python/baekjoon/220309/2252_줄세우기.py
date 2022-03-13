import sys
sys.stdin = open('input.txt')

# 내가 못품

# 원본 https://sungmin-joo.tistory.com/83
# a, b를 입력받을 때 a가 b를 참조한다고 생각하고, 참조 횟수가 0인 정점부터 위상 정렬을 수행
# 다만 참조 횟수가 0인 정점에 대해 정렬을 수행하고 나서 해당 정점이 참조하던 또 다른 정점에 대해 참조 횟수를 감소시켜주는 작업을 꼭 수행

from collections import deque

n, m = map(int, input().split())
arr = []
inDegree = [0 for i in range(32001)]
graph = [[] for i in range(32001)]
queue = deque()

for i in range(m):
    a, b = map(int, input().split())
    arr.append([a, b])

for a, b in arr:
    inDegree[b] += 1
    graph[a].append(b)

for i in range(1, n + 1):
    if inDegree[i] == 0:
        queue.append(i)

while queue:
    student = queue.popleft() #indegree가 0인 정점을 제거하고, 해당 정점이 참조하고있던 점들의 indegree를 감소시킨다.
    for j in graph[student]:
        inDegree[j] -= 1
        if inDegree[j] == 0:
            queue.append(j)
    print(student, end = ' ')


# # 패작1 소요시간 58분
# N, M = map(int, input().split())    # 1부터 N번까지 학생들의 번호있음. M은 키를 비교한 횟수 # A가 B앞에 서야함
# temp = []
# # temp 리스트 생성
# # 매번 temp 안의 숫자들과 input 숫자들과 대조
# # 같은 숫자가 temp 안에 있으면, 다른 숫자를 크면 앞에 작으면 뒤에 입력
# # 이걸 반복
# # 언급이 안된 숫자는 그냥 맨 앞에 입력
# check = [0] * N
#
# for i in range(M):
#     A, B = map(int, input().split())
#     if temp:
#         if A in temp and B not in temp:
#             for j in range(len(temp)):
#                 if temp[j] == A:
#                     temp.insert(j+1, B)
#                     check[B-1] = 1
#                     break
#         if B in temp and A not in temp:
#             for j in range(len(temp)):
#                 if temp[j] == B:
#                     temp.insert(j, A)
#                     check[A-1] = 1
#                     break
#     else:
#         temp.append(A)
#         temp.append(B)
#         check[A - 1], check[B - 1] = 1, 1
#
# for i in range(len(check)):
#     if check[i] == 0:
#         temp.insert(0, i+1)
#
# print(check)
# print(*temp)