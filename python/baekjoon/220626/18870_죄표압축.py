import sys
sys.stdin = open('input.txt')


N = int(input())
nums = list(map(int, input().split()))                  # O(N)
no_overlap_nums = set(nums)                             # O(N)
s_no_overlap_nums = list(sorted(no_overlap_nums))       # 퀵 정열과 동작 방식이 비슷한 병합 정렬을 기반으로 만들어짐
                                                        # 퀵정렬보다 느리지만 최악의 경우에도 시간복잡도 O(NlogN)을 보장
dic = dict()
for i in range(len(s_no_overlap_nums)):                 # 딕셔너리를 자료형을 활용해서 순서대로 정렬된 상태의 각 숫자들의 index 위치를 기록
    dic[s_no_overlap_nums[i]] = i                       # O(1) * N = O(N)

for i in nums:                                          # 기록한 정렬된 상태에서의 index 위치를 활용하여, 잇풋 리스트의 각 원소값을 출력
    print(dic[i], end=" ")                              # O(1) * N 시간 복잡도




# def countingSort(array):
#     L = len(array)
#     occurances_cnt = [0] * (max(array)+1)
#
#     # count the occurances of each element in the arrary
#     for i in range(L):
#         occurances_cnt[array[i]] += 1
#
#     # adding each element to the right of it accumulatively
#     for i in range(1, len(occurances_cnt)):
#         occurances_cnt[i] += occurances_cnt[i-1]
#
#     # shifting the whole arrary to right side one index
#     for i in range(len(occurances_cnt)-1, 0, -1):
#         occurances_cnt[i] = occurances_cnt[i-1]
#     occurances_cnt[0] = 0
#
#     # check for the distorting index number for each element in the original array
#     # and record the starting index on a new array
#     output = [0] * len(array)
#     for i in range(len(array)):
#         output[occurances_cnt[array[i]]] = array[i]
#         occurances_cnt[array[i]] += 1
#
#     return output
#
# N = int(input())
# nums = list(map(int, input().split()))          # O(N)
#
# min_num = min(nums)
# if min_num < 0:
#     for i in range(N):
#         nums[i] += abs(min_num)
# elif min_num > 0:
#     for i in range(N):
#         nums[i] -= min_num
#
# s_array = countingSort(nums)                    # 인풋 리스트 정렬
# temp = [i for n, i in enumerate(s_array) if i not in s_array[:n]]   # 정렬 리스트 중복제거
#
# for i in range(N):                                      # O(N)
#     print(temp.index(nums[i]), end=" ")    # O(1) + O(1)
# # total = O(N+k)




# N = int(input())
# nums = list(map(int, input().split()))                  # O(N)
# s_no_overlap_nums = sorted(set(nums))                   # O(NlogN) + O(N) = O(NlogN)
#
#
# for i in range(N):                                      # O(N)
#     print(s_no_overlap_nums.index(nums[i]), end=" ")    # O(1) + O(1)
# total = O(NlogN)
# 이것도 통과 안되는걸 보면 O(N) 으로 풀어야된다는건데.. sorting 부분을 counting sort 로 바꾸면 되지 않을까




# N = int(input())
# nums = list(map(int, input().split()))                  # O(N)
# no_overlap_nums = set(nums)                             # O(N)
# s_no_overlap_nums = sorted(no_overlap_nums)             # 퀵 정열과 동작 방식이 비슷한 병합 정렬을 기반으로 만들어짐
#                                                         # 퀵정렬보다 느리지만 최악의 경우에도 시간복잡도 O(NlogN)을 보장
# for i in range(N):
#     print(s_no_overlap_nums.index(nums[i]), end=" ")      # O(N) * N 시간 복잡도




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