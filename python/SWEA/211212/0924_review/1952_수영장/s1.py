'''
총 소요시간 2시간 12분 33초
thought process: 22분 40초
부분집합 찾듯이, 피벗을 이동 시키며, 해당 원소와 표 값들을 곱하여
모든 원소를 다 돌았을때, 가장 작은 값을 ans 에 갱신시켜주면 답

월별 인덱스에 접근 =>
각 인덱스에 일, 월, 분기 순으로 가격 적용 =>
순열을 생성하며 최소값을 ans에 갱신
'''

import sys
sys.stdin = open('input.txt')

# def powerset(month, price):
#     global ans
#
#     if month > 12:
#         if price < ans:
#             ans = price
#         return
#
#     else:
#         if months[month]:                                       # 월 출석일이 0 이 아닐때
#             powerset(month + 1, price + (months[month] * d))    # + daily price
#             powerset(month + 1, price + m)                      # + month price
#             powerset(month + 3, price + q)                      # + quarter price
#         else:
#             powerset(month + 1, price)
#
#
# for tc in range(1, int(input())+1):
#     d, m, q, y = map(int, input().split())
#     months = [0] + list(map(int, input().split()))      # 첫 [0]는 인덱싱 위한 dummy
#     ans = y
#     for i in range(13):            # 12개월 범위 지정
#         if months[i]:
#             powerset(i, 0)   # 현재 월, 총 가격
#             break
#     print('#{} {}'.format(tc, ans))


for tc in range(1, int(input())+1):

    d, m, q, y = map(int, input().split())
    months = [0] + list(map(int, input().split()))
    dp = [0] * 13

    dp[1] = min(m, months[1]*d)
    dp[2] = dp[1] + min(m, months[2]*d)

    for i in range(3, 13):
        dp[i] = min(dp[i-3] + q, dp[i-1] + m, dp[i-1] + (months[i] * d))

    print('#{} {}'.format(tc, min(dp[12], y)))





















