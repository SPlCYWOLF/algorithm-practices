import sys
sys.stdin = open('input.txt')
from itertools import combinations, product, permutations

# sum()함수 없이 패작4 방식을 활용해보자
# 아 모르겠다 포기선언
demand = int(input())
m, n = map(int, input().split())
pm = [int(input()) for _ in range(m)] * 2
pn = [int(input()) for _ in range(n)] * 2
ans = 0

chances1, chances2 = [[] for _ in range(m)], [[] for _ in range(n)]
for i in range(m):
    if pm[i] == demand:
        ans += 1
        continue
    if pm[i] > demand:
        continue

    for j in range(i+1, i+m):
        chances1[i].append(pm[i:j])

for i in range(n):
    if pn[i] == demand:
        ans += 1
        continue
    if pn[i] > demand:
        continue

    for j in range(i+1, i+n):
        chances2[i].append(pn[i:j])



# for i in range(len(chances1)):
#     if chances1[i] == 0:
#         continue
#     if i + chances2[demand-i]:
#         ans += chances1[i] * chances2[demand-i]

print(chances1)
print(chances2)
print(ans)





# 패작5 : 피자1과 피자2의 7보다 작은 경우의 수를 리스트에 다 저장하고 합해주는 접근 방식은
# sum() 함수를 활용하는데, 이건 O(n) 시간복잡도여서 결국 전체적으로 O(n^3)가 되어버려
# 시간초과로 실패한듯하다.
# demand = int(input())
# m, n = map(int, input().split())
# pm = [int(input()) for _ in range(m)] * 2
# pn = [int(input()) for _ in range(n)] * 2
# ans = 0
#
# chances1, chances2 = [0] * (demand+1), [0] * (demand+1)      # 인덱스 == 피자크기의 합
# for i in range(m):
#     for j in range(i+1, i+m):
#         S = sum(pm[i:j])
#         if S == demand:
#             ans += 1
#             continue
#         if S < demand:
#             chances1[S] += 1
#
# for i in range(n):
#     for j in range(i+1, i+n):
#         S = sum(pn[i:j])
#         if S == demand:
#             ans += 1
#             continue
#         if S < demand:
#             chances2[S] += 1
#
# for i in range(len(chances1)):
#     if chances1[i] == 0:
#         continue
#     if i + chances2[demand-i]:
#         ans += chances1[i] * chances2[demand-i]
#
# print(chances1)
# print(chances2)
# print(ans)




# 패작4 : 필살기 4중 for문으로 시간초과
# demand = int(input())
# m, n = map(int, input().split())
# pm = [int(input()) for _ in range(m)] * 2
# pn = [int(input()) for _ in range(n)] * 2
# ans = 0
#
# for i in range(m):
#     for j in range(i+1, m+i):
#         if sum(pm[i:j]) == demand:
#             ans += 1
#             continue
#         if sum(pm[i:j]) > demand:
#             continue
#
#         for k in range(n):
#             for l in range(k+1, n+k):
#                 if sum(pn[k:l]) == demand:
#                     ans += 1
#                     continue
#                 if sum(pm[i:j] + pn[k:l]) == demand:
#                     ans += 1
#
#
# if sum(pm[:m]) == demand:
#     ans += 1
# if sum(pn[:n]) == demand:
#     ans += 1
# if sum(pm[:m] + pn[:n]) == demand:
#     ans += 1
#
# print(ans)





# 패작3 : 메모리 초과
demand = int(input())
m, n = map(int, input().split())
pm = [int(input()) for _ in range(m)] * 2
pn = [int(input()) for _ in range(n)] * 2
ans = 0
pizza1, pizza2 = [], []
for i in range(m):
    for j in range(i+1, m+i):
        if sum(pm[i:j]) == demand:
            ans += 1
        elif sum(pm[i:j]) > demand:
            continue
        pizza1.append(pm[i:j])

for i in range(n):
    for j in range(i+1, n+i):
        if sum(pn[i:j]) == demand:
            ans += 1
        elif sum(pn[i:j]) > demand:
            continue
        pizza2.append(pn[i:j])

for p1 in pizza1:
    for p2 in pizza2:
        if sum(p1+p2) == demand:
            ans += 1

if sum(pm[:m]+pn[:n]) == demand:
    ans += 1

print(pizza1)
print(pizza2)
print(ans)





# 패작2 : 2조각 이상 판매시 반드시 연속된 조각 팔앙야함, 고로 두 피자 조각들을 합쳐서 푸는건 불가능
# demand = int(input())
# m, n = map(int, input().split())
# pm = [int(input()) for _ in range(m)]
# pn = [int(input()) for _ in range(n)]
# pizza = pm + pn
# print(pizza)
#
# ans = 0
#
# for i in range(1, m + n + 1):
#     comb = sorted(list(combinations(pizza, i)))
#     print(comb)
#     for c in comb:
#         if sum(c) == demand:
#             ans += 1
# print(ans)





# 패작 1
# 리스트 융합해서 permutation 구해보자

# demand = int(input())
# m, n = map(int, input().split())
# pm = [int(input()) for _ in range(m)]
# pn = [int(input()) for _ in range(n)]
#
# ans = 0
#
# for i in range(1, m+1):
#     # print(list(combinations(pm, i)))
#     temp_pm = list(combinations(pm, i))
#     temp_pm = [list(e) for e in temp_pm]
#
#     for c1 in temp_pm:
#         if sum(c1) == demand:
#             ans += 1
#
#     for j in range(1, n+1):
#         # print(list(combinations(pn, j)))
#         temp_pn = list(combinations(pn, j))
#         # print(temp_pn)
#         temp_pn = [list(e) for e in temp_pn]
#
#
#         for c2 in temp_pn:
#             if sum(c2) == demand:
#                 ans += 1
#
#         for c3 in temp_pm:
#             for c4 in temp_pn:
#                 zipped = zip(c3, c4)
#                 print(*list(zipped))
#                 for c5 in zipped:
#                     # print(c5)
#                     # print(sum(c5))
#                     if sum(c5) == demand:
#                         ans += 1
#
# print(ans)


# a  b  c  f  g  h   6

# af  ag  ah  afg  agh  ahf  afgh   7
# bf  bg  bh  bfg  bgh  bhf  bfgh   7
# cf  cg  ch  cfg  cgh  chf  cfgh   7

# fa  fb  fc  fab  fbc  fca  fabc   4
# ga  gb  gc  gab  gbc  gca  gabc   4
# ha  hb  hc  hab  hbc  hca  habc   4

# abfg  abgh  abhf  abfgh   4
# bcfg  bcgh  bchf  bcfgh   4
# cafg  cagh  cahf  cafgh   4
# abcfg  abcgh  abchf  abcfgh   4

# fgabc   1
# ghabc   1
# hfabc   1