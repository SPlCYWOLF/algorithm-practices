import sys
sys.stdin = open('input.txt')

# 소요시간 95분..

H, W = map(int, input().split())
height = list(map(int, input().split()))
ans = 0

arr = [[0]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if height[j] <= i:
            arr[i][j] = 1
print(arr)

# 2차원 배열 탐색하며 고이지 않은 부분 제거
for i in range(H-1, -1, -1):
    wall, cnt, go = 0, 0, False
    if arr[i].count(0) <= 1:
        pass
    else:
        for j in range(W-1, -1, -1):
            if arr[i][j] == 0:
                go = True
                wall += 1
            if wall == 2:
                if cnt == 0:
                    wall = 1
                else:
                    ans += cnt
                    cnt = 0
                    wall = 1
            elif wall == 1 and arr[i][j] == 1:
                cnt += 1

print(ans)



# 패작
# H, W = map(int, input().split())
# height = list(map(int, input().split()))
# ans = 0
#
# arr = [[0]*W for _ in range(H)]
# for i in range(H):
#     for j in range(W):
#         if height[j] <= i:
#             arr[i][j] = 1
# print(arr)
#
# # 2차원 배열 탐색하며 고이지 않은 부분 제거
# for i in range(H-1, -1, -1):
#     go, check, cnt = True, 0, 0
#     for j in range(W-1, -1, -1):
#         if j == W-1 and arr[i][j]:
#             go = False
#         elif arr[i][j] == 0:
#             go = True
#             check += 1
#         else:
#             if go:
#                 if arr[i][j]:
#                     cnt += 1
#                 else:
#                     check += 1
#                 if check <= 2:
#                     ans += cnt
#                     check = 0
#
# print(ans)


