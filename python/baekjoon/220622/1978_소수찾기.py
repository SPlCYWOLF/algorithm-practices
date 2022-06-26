import sys
sys.stdin = open('input.txt')


N = int(input())
nums = list(map(int, input().split()))
ans = 0

for i in range(N):
    if nums[i] > 1:
        if nums[i] == 2:
            ans += 1
        elif nums[i] == 3:
            ans += 1
        elif nums[i] == 5:
            ans += 1
        elif nums[i] == 7:
            ans += 1
        elif nums[i] == 11:
            ans += 1
        elif nums[i] == 13:
            ans += 1
        elif nums[i] == 17:
            ans += 1
        elif nums[i] == 19:
            ans += 1
        elif nums[i] == 23:
            ans += 1
        elif nums[i] == 29:
            ans += 1
        else:
            if nums[i] % 2 != 0 and nums[i] % 3 != 0 and nums[i] % 5 != 0 and nums[i] % 7 != 0 and nums[i] % 11 != 0 and nums[i] % 13 != 0 and nums[i] % 17 != 0 and nums[i] % 19 != 0 and nums[i] % 23 != 0 and nums[i] % 29 != 0:
                ans += 1
                print(nums[i])

print(ans)