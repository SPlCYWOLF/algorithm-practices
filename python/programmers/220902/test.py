import sys
sys.stdin = open('input.txt')
from collections import defaultdict


# bfs로 섬 탐색하며, 해당 섬의 둘레를 기록
# 가장 큰 둘레 기록

# 위치 이동은 방향델타 값 활용하여 상->우->하->좌 순으로 순회
# 다음 위치로 이동 불가능하면, 둘레 +1 로 둘레 기록

# 방문 여부는 visited로 기록

# from collections import deque
#
# dr = (-1, 0, 1, 0)
# dc = (0, 1, 0, -1)
# visited = [[0] * 50 for _ in range(50)]
#
#
# def bfs(r, c, h, w, maps):
#     global visited
#     visited[r][c] = 1  # 새로 방문한 섬의 방문체크
#     perimeter = 0  # 새로 방문한 섬의 둘레 값 초기화
#
#     Q = deque()
#     Q.append((r, c))
#     while Q:
#         r, c = Q.popleft()
#         for k in range(4):  # 다음 이동 경로 상->우->하->좌 탐색
#             nr, nc = r + dr[k], c + dc[k]  # 새로운 좌표값 선언
#
#             if 0 <= nr < h and 0 <= nc < w:  # 다음 좌표가 범위 내에 있고
#                 if not visited[nr][nc]:  # 아직 방문하지 않았고
#                     if maps[nr][nc]:  # 섬이라면
#                         visited[nr][nc] = 1  # 방문 및 방문체크
#                         Q.append((nr, nc))
#                     else:
#                         perimeter += 1  # 해안바다라면 둘레 + 1
#             else:
#                 perimeter += 1  # 지도의 경계부분이라면 둘레 + 1
#
#     return perimeter
#
#
# def solution(maps):
#     largest_perimeter = 0  # 섬의 최고 둘레값 초기화
#
#     H = len(maps)  # 지도의 높이 값
#     for i in range(H):
#         W = len(maps[i])  # 지도의 너비 값
#         for j in range(W):
#             if not visited[i][j] and maps[i][j]:  # 방문하지 않았고 섬이면,
#                 largest_perimeter = max(largest_perimeter, bfs(i, j, H, W, maps))  # bfs 활용한 섬의 둘레 탐색 및 최고 둘레 갱신
#
#     return largest_perimeter







# from collections import defaultdict
#
#
# def solution(orders):
#
#     customers = defaultdict(set)    # key: 이름, value: set() 로 dictionary활용하여 주문 음식 관리
#
#     for order in orders:            # 가장 먼저, 사람의 주문 기록 customers(딕셔너리)에 추가
#         order_detail = order.split(" ")         # orders 를 " " 기준으로 나눈 후 리스트로 변환
#
#         candidate = order_detail[0]             # dictionary의 key 값 (이름)
#         order_detail = set(order_detail[1::])   # dictionary의 value 값 (중복없앤 음식)
#
#         customers[candidate] |= order_detail    # set으로 이루어진 value에 set값을 더해줌
#
#     max_len = -1            # 최고 주문 음식 종류 개수
#     hall_of_fame = []       # 가장많이 먹은 이름 저장
#     for name, food in customers.items():    # 딕셔너리를 loop하며 최고 많은 음식종류 주문자 판별
#         L = len(food)
#
#         if L > max_len:                     # 최고많은 종류 주문을 했으면
#             hall_of_fame = [name]           # 최강 등극
#             max_len = L                     # 최고 주문 음식 종류 개수 갱신
#             continue
#         if L == max_len:                    # 최고와 어깨를 나란히 했다면,
#             hall_of_fame += [name]          # 이름만 추가
#
#     return sorted(hall_of_fame)
# ---------------------------------------------------------------------------------------------
#
# temp = ["alex pizza pasta steak", "bob noodle sandwich pasta", "choi pizza sandwich pizza", "alex pizza pasta steak"]
#
# customers = defaultdict(set)
#
# for t in temp:
#     order_detail = t.split(" ")
#     candidate = order_detail[0]
#     order_detail = set(order_detail[1::])
#
#     customers[candidate] |= order_detail
#
# max_len = -1
# hall_of_fame = []
# for name, food in customers.items():
#     L = len(food)
#     print(L)
#     if L > max_len:
#         hall_of_fame = [name]
#         max_len = L
#         continue
#     if L == max_len:
#         hall_of_fame += [name]
#
# print(customers)
#
# print(sorted(hall_of_fame))









# "+"로 시작되고
# 총 길이가 16이고
# "-"로 나누었을때 최소 길이가 2, 최고 길이가 4이고
#  그 외의 길이가 없으면 return 3
# 아니면 return -1

# 유형3이 아니고 4번째 자리에 "-"가 오고
# 총 길이가 13이고
# "-"로 나누었을때 최소 길이가 3, 최고 길이가 4이고
# 그 외의 길이가 없으면 return 1
# 아니면 return -1

# 유형 3, 1 이 아니고
# 총 길이가 11이고
# "-"가 없으면 return 2
# 아니면 return -1

# def findMinMax(array, min_limit, max_limit, ans_type):
#     min_exist, max_exist = 0, 0
#     for a in array:
#         L = len(a)
#         if L < min_limit or L > max_limit:
#             return -1
#         if L == max_limit:
#             max_exist += 1
#             continue
#         if L == min_limit:
#             min_exist += 1
#
#     if min_exist and max_exist:
#         return ans_type
#     else:
#         return -1
#
#
# def solution(phone_number):
#     if phone_number[0] == "+":
#         if len(phone_number) == 16:
#             temp = phone_number.split("-")
#             return findMinMax(temp, 2, 4, 3)  # "-"로 나눈 리스트, 필요한 길이(최소), 필요할 길이(최고), 유형
#         return -1
#
#     if phone_number[3] == "-":
#         if len(phone_number) == 13:
#             temp = phone_number.split("-")
#             return findMinMax(temp, 3, 4, 1)  # "-"로 나눈 리스트, 필요한 길이(최소), 필요할 길이(최고), 유형
#         return -1
#
#     if len(phone_number) == 11:
#         if "-" not in phone_number:
#             return 2
#     return -1
# ----------------------------------------------------------------------------------------
#
# split("-") 을 해서 key:길이, value:개수 로 축적해서
# {3: 1, 4: 2} 이면 유형 1
# "+"가 없고 {11: 1} 이면 유형 2
# "+"가 있고 {2: 2, 4: 2} 이면 유형 3

# temp = "+82-10-1212-3333"
# w = temp[0]
# phone_dict = defaultdict(int)
# temp = temp.split("-")
# for t in temp:
#     phone_dict[len(t)] += 1
# print(phone_dict)
#
# if w == "+" and phone_dict[2] == 1 and phone_dict[3] == 1 and phone_dict[4] == 2:
#     print(3)
# else:
#     print(-1)


# split("-") 을 해서 key:길이, value:개수 로 축적해서
# {3: 1, 4: 2} 이면 유형 1
# "+"가 없고 {11: 1} 이면 유형 2
# "+"가 있고 {2: 2, 4: 2} 이면 유형 3

# from collections import defaultdict
#
#
# def solution(phone_number):
#
#     phone_dict = defaultdict(int)
#     number_list = phone_number.split("-")
#     for n in number_list:
#         phone_dict[len(n)] += 1
#
#     if phone_number[0] != "+" and phone_dict[3] == 1 and phone_dict[4] == 2:
#         return 1
#     if phone_number[0] != "+" and phone_dict[11] == 1:
#         return 2
#     if phone_number[0] == "+" and phone_dict[2] == 2 and phone_dict[4] == 2:
#         return 3
#
#     return -1


# temp = "010-1212-3333"
# phone_dict = dict()
# for t in range(len(temp)):
#     phone_dict[t] = temp[t]
# print(phone_dict)

#
# temp = temp.split("-")
# print(temp)
#
# max_len, min_len = -1, 9999999999
# for t in temp:
#     L = len(t)
#
#     if L < 3 or L > 4:
#         print(False)
#         break
#     if L > max_len:
#         max_len = L
#     if L < min_len:
#         min_len = L