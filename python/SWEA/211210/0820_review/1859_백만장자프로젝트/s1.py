import sys
sys.stdin = open('input.txt')

# 1차 try 실패 ㅎ
# def dfs(arr):
#     global ans
#     if len(arr) > 1:
#         big_num = max(arr)
#         for j in range(arr.index(big_num)):
#             ans += big_num - arr[j]
#         dfs(arr[arr.index(big_num):-1])
#     else:
#         print('#{} {}'.format(tc, ans))


for tc in range(1, int(input())+1):
    
#     N = int(input())
#     nums = tuple(map(int, input().split()))
#     max_num = max(nums)

#     ans = 0

#     for i in range(nums.index(max_num)):
#         ans += max_num-nums[i]
#     # print(ans)
#     dfs(nums[nums.index(max_num):-1])



# 교수님 풀이 참고
    N = int(input())
    sales = list(map(int, input().split()))
    ans = 0
    max_val = sales[N-1]                # 혹은 sales[-1]
    for i in range(N-2, -1, -1):        # 최댓값으로 둔 마지막 날 전날부터 시작하여 최댓값을 갱신
        if max_val > sales[i]:          # 최댓값보다 작은 경우
            ans += max_val - sales[i]   # 차액 만큼 이익을 남길 수 있음
        else:                           # 최댓값보다 큰 경우
            max_val = sales[i]          # 팔아도 이익이 없기 때문에 max_val 갱신
    print('#{} {}'.format(tc, ans))