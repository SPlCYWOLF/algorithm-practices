import sys
sys.stdin = open('input.txt')


'''
dfs 활용하여 각 부분집합 요소들의 원소들의 합 구하기
'''


# def dfs(k):
#
#     if k == N:
#         return
#
#     for i in range(k, N):
#         if not visited[i]:
#             visited[i] = 1
#             tmp[k] = nums[i]
#             score = sum(tmp)
#             ans.add(score)
#             dfs(k+1)
#             visited[i] = 0
#             tmp[k] = 0
# -------------------------------------------------
# def dfs(score, k):
#
#     if k == N:
#         return
#
#     else:
#         for i in range(k, N):
#             if not visited[i]:
#                 visited[i] = 1
#                 ans.add(score+nums[i])
#                 dfs(score+nums[i], k+1)
#                 visited[i] = 0

def dfs(score, k):            # 부분집합
    if k == N:
        return

    else:
        for i in range(k, N):
            if not visited[i]:
                visited[i] = 1
                ans.add(score+nums[i])
                dfs(score+nums[i], k+1)
                visited[i] = 0


for tc in range(1, int(input())+1):

    N = int(input())
    nums = tuple(map(int, input().split()))
    tmp = [0] * N
    visited = [0] * N
    ans = set()
    
    dfs(0, 0)    # 현재 점수, dfs 깊이
    print('#{} {}'.format(tc, len(ans)+1))
    # print(ans)