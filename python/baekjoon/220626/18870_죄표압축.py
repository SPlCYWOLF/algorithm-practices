import sys
sys.stdin = open('input.txt')

N = int(input())
nums = list(map(int, input().split()))                  # O(N)
s_no_overlap_nums = sorted(set(nums))                   # O(NlogN) + O(N) = O(NlogN)

for i in range(N):                                      # O(N)
    print(s_no_overlap_nums.index(nums[i]), end=" ")    # O(1)

# total = O(NlogN) 이것도 통과 안되는걸 보면 O(N) 으로 풀어야된다는건데.. 너무하네 ㅇㅅㅇ



# N = int(input())
# nums = list(map(int, input().split()))                  # O(N)
# no_overlap_nums = set(nums)                             # O(N)
# s_no_overlap_nums = sorted(no_overlap_nums)             # 퀵 정열과 동작 방식이 비슷한 병합 정렬을 기반으로 만들어짐
#                                                         # 퀵정렬보다 느리지만 최악의 경우에도 시간복잡도 O(NlogN)을 보장
# for i in range(N):
#     print(s_no_overlap_nums.index(nums[i]), end=" ")      # O(1) * N 시간 복잡도




# N = int(input())
# nums = list(map(int, input().split()))
# zip_nums = [0] * N                                      # O(N)
# no_overlap_nums = set(nums)                             # O(N)
# s_no_overlap_nums = sorted(no_overlap_nums)             # 퀵 정열과 동작 방식이 비슷한 병합 정렬을 기반으로 만들어짐
#                                                         # 퀵정렬보다 느리지만 최악의 경우에도 시간복잡도 O(NlogN)을 보장
# for i in range(N):
#     zip_nums[i] = s_no_overlap_nums.index(nums[i])      # O(1) * N 시간 복잡도
#
# print(*zip_nums)



# N = int(input())
# nums = list(map(int, input().split()))
# zip_nums = [0] * N
#
# for i in range(N):
#     temp_bag = [0] * N
#     target = nums[i]
#     cnt = 0
#     for j in range(N):
#         if target > nums[j] and nums[j] not in temp_bag:
#             temp_bag[j] = nums[j]
#             cnt += 1
#     zip_nums[i] = cnt
#
# print(*zip_nums)