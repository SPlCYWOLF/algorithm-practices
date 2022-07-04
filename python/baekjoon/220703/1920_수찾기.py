import sys
sys.stdin = open("input.txt")

def finder(n):
    global nums
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2

        if nums[mid] == n:
            return 1
        elif nums[mid] < n:
            start = mid + 1
        else:
            end = mid - 1

    return 0

N = int(input())
nums = sorted(list(map(int, input().split())))
M = int(input())
candidates = list(map(int, input().split()))

ans = map(finder, candidates)
print(*ans)



# for i in range(M):
#     target = candidates[i]
#     if target in nums:
#         print(1, end=" ")
#     else:
#         print(0, end=" ")