from collections import deque
import sys
sys.stdin = open('input.txt')

# 패작 2 : 42% 시간초과
T, A, B = map(int, input().split())
max_fullness = 0
foods = [A, B]

Q = deque()
Q.append((0, False))     # 음식, 배부름 수치, 소화 여부
Q.append((0, False))
found = False

while Q and not found:
    fullness, digested = Q.popleft()
    max_fullness = max(max_fullness, fullness)

    for i in range(2):
        if fullness + foods[i] == T:
            max_fullness = fullness + foods[i]
            found = True
            break
        elif fullness + foods[i] < T:
            Q.append((fullness + foods[i], digested))

        elif not digested and (fullness // 2) + foods[i] == T:
            max_fullness = (fullness // 2) + foods[i]
            found = True
            break
        elif not digested and (fullness // 2) + foods[i] < T:
            Q.append((fullness // 2 + foods[i], True))

print(max_fullness)


# 패작 1 : 39% 시간초과
# while Q:
#     food, fullness, digested = Q.popleft()
#     if fullness + food <= T:
#         fullness += food
#
#         if fullness == T:
#             max_fullness = fullness
#             break
#         else:
#             max_fullness = max(max_fullness, fullness)
#             for i in range(2):
#                 Q.append((foods[i], fullness, digested))
#
#     else:
#         if not digested and (fullness // 2) + food <= T:
#             digested = True
#             fullness = fullness // 2 + food
#
#             if fullness == T:
#                 max_fullness = fullness
#                 break
#             else:
#                 max_fullness = max(max_fullness, fullness)
#                 for i in range(2):
#                     Q.append((foods[i], fullness, digested))
#
# print(max_fullness)