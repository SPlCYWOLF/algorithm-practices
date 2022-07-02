import sys
sys.stdin = open('input.txt')


N, K = map(int, input().split())
coins = list(int(input()) for _ in range(N))
s_coins = sorted(coins, reverse=True)
cnt = 0

for i in range(N):

    if K == 0:
        break

    target = s_coins[i]

    if (K - target) >= 0:
        cnt += K // target
        K = K % target

print(cnt)



# for i in range(N):
#     target = s_coins[i]
#     K_string, s_target = str(K), str(target)
#
#     if (K - target) >= 0:
#         cnt += int(K_string[0]) // int(s_target[0])
#         K -= target * (int(K_string[0]) // int(s_target[0]))
#
# print(cnt)



# N, K = map(int, input().split())
# coins = list(int(input()) for _ in range(N))
# s_coins = sorted(coins, reverse=True)
# cnt = 0
#
# for i in range(N):
#     target = s_coins[i]
#
#     while (K - target) >= 0:
#         K -= target
#         cnt += 1
#
# print(cnt)