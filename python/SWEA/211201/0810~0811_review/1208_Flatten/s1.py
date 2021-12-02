import sys
sys.stdin = open('input.txt')


# 가장 높은 것 찾고 하나 빼고 해당 값 해당 위치에 replace
# 가장 낮은거 찾고 하나 더하고 해당 값 해당 위치에 replace
# 위의 과정 dump 획수만큼 무한 반복
# 마지막에 최대값 - 최소값 반환

for tc in range(1, 11):
    
    dump = int(input())
    nums = list(map(int, input().split()))
    
    for _ in range(dump):
        i = nums.index(max(nums))
        j = nums.index(min(nums))
        
        if (nums[i] - nums[j]) == 0:
            break
        else:
            nums[i] -= 1
            nums[j] += 1

    ans = max(nums) - min(nums)

    print('#{} {}'.format(tc, ans))
