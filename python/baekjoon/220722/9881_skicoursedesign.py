from collections import deque
import sys
sys.stdin = open('input.txt')

# 완전탐색으로 가보자
# 언덕 높이는 최대 100 까지.
# 0-17, 1-18, 2-19 이런 식으로 83번 loop 돌면서
# 모든 리스트를 해당 범위에 맞추면서 발생한 cost의 minimum 값을 정답으로 반환

N = int(input())
hills = tuple(int(input()) for _ in range(N))
min_cost = 9999999999

for i in range(84):
    min_h, max_h = i, i+17
    cost = 0
    for hill in hills:
        if hill < min_h:
            cost += (min_h - hill) ** 2
        if hill > max_h:
            cost += (hill - max_h) ** 2
    min_cost = min(min_cost, cost)

print(min_cost)



# 패작 3
# 가운데부터 비교하며 높이를 반반 나눠서 높이를 줄여가는 풀이 실패
# brute force로 풀어야하는 문제였다.. 그리디한 풀이는 불가능했다
# N = int(input())
# temp = [0] * N
# for i in range(N):
#     temp[i] = int(input())
# heights = sorted(temp)
# print(heights)
#
# mid = (len(heights) // 2) - 1
# if len(heights) % 2:
#     mid = len(heights) // 2
#
# left, right = 0, 0
# cost, turn = 0, True
# for i in range(N-1):
#     l, r = mid-left, mid+1+right
#     l_h, r_h = heights[l], heights[r]
#     new_l_h, new_r_h = 0, 0
#
#     if r_h - l_h > 17:
#         difference = (r_h - l_h) - 17
#
#         if difference % 2:
#             cost += ((difference // 2) ** 2) + (((difference // 2) + 1) ** 2)
#             new_l_h = l_h + (difference // 2)
#         else:
#             cost += ((difference // 2) ** 2) + ((difference // 2) ** 2)
#             new_l_h = l_h + (difference // 2 + 1)
#         new_r_h = r_h - (difference // 2)
#     else:
#         if turn:
#             turn = False
#             left += 1
#         else:
#             turn = True
#             right += 1
#         continue
#
#     heights.pop(l)
#     heights.pop(r-1)
#     heights.append(new_l_h)
#     heights.append(new_r_h)
#     heights.sort()
#
#     if turn:
#         turn = False
#         left += 1
#     else:
#         turn = True
#         right += 1
# print(heights)
# print(cost)





# 패작2
# 양 끝부분부터 비교하며 높이를 반반 나눠서 줄여가는 풀이
# N = int(input())
# temp = [0] * N
# for i in range(N):
#     temp[i] = int(input())
# temp = sorted(temp)
# heights = deque()
# heights += temp
# # print(heights)
#
# cost = 0
# l, r = 0, N
# while True:
#     min_h, max_h = heights.popleft(), heights.pop()
#     difference = max_h - min_h
#     if difference <= 17:
#         break
#
#     difference = difference - 17
#     if difference % 2:
#         cost += ((difference // 2) ** 2) + (((difference // 2) + 1) ** 2)
#         new_min_h = min_h + (difference // 2)
#     else:
#         cost += ((difference // 2) ** 2) + ((difference // 2) ** 2)
#         new_min_h = min_h + (difference // 2 + 1)
#     new_max_h = max_h - (difference // 2)
#
#     min_done, max_done = False, False
#     for i in range(N-2):
#         if not min_done and heights[i] > new_min_h:
#             min_done = True
#             heights.insert(i, new_min_h)
#         if not max_done and heights[(N-3)-i] < new_max_h:
#             max_done = True
#             heights.insert((N-1)-i, new_max_h)
# print(cost)





# 그냥 패작1
# N = int(input())
# min_h, max_h = 9999999999, 0
# for i in range(N):
#     h = int(input())
#     if h < min_h:
#         min_h = h
#     if h > max_h:
#         max_h = h
#
# height = max_h - min_h
# height = height - 17
#
# if height % 2:
#     print(((height // 2) ** 2) + (((height // 2) + 1) ** 2))
# else:
#     print(((height // 2) ** 2) + ((height // 2) ** 2))
