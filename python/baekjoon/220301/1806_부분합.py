import sys
sys.stdin = open('input.txt')
# 총 투자 시간 : 60분
# 반례 모음 https://bingorithm.tistory.com/13

# 패작2 : 시간초과
# for loop 돌며 S보다 같거나 커질때까지 더하기
# cnt 로 더한 횟수 기록

# N, S = map(int, input().split())
# nums = list(map(int, input().split()))
# tmp_list = []
#
# for i in range(N):
#     temp, cnt = 0, 1
#     if nums[i] >= S:
#         tmp_list.append(cnt)
#         break
#     else:
#         for j in range(i, N-1):
#             if (temp + nums[j]) >= S:
#                 tmp_list.append(cnt)
#                 break
#             else:
#                 temp += nums[j]
#                 cnt += 1
#
# print(min(tmp_list))



# 패작1 : 문제 이해 못함
# 숫자들 거꾸로 정렬
# 하나씩 더해가며 S와 대조
# S와 같거나 크면 더한 횟수 반환
# 연속적으로 작아지는 숫자가 아니면, temp 바로 다음걸로 바꾸고 cnt 도 초기화

# N, S = map(int, input().split())
# nums = list(map(int, input().split()))
# nums = sorted(nums)
# temp, cnt = 0, 0
# ans = 0
#
# for i in range(N):
#     if i == 0:                          # 처음 수 일 경우
#         if nums[i] >= S:
#             ans = nums[i]
#             break
#         else:
#             temp += nums[i]
#             cnt += 1
#     else:
#         if nums[i] == (nums[i-1]-1):    # 연속된 수 인 경우
#             temp += nums[i]
#             cnt += 1
#             if temp >= S:
#                 ans = nums[i]
#                 break
#         else:                           # 연속된 수 아닌 경우
#             temp = nums[i]
#             cnt = 1
#             if temp >= S:
#                 ans = nums[i]
#                 break
# print(nums)
# print(cnt)