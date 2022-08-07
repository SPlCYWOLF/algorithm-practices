import sys
sys.stdin = open('input.txt')
from itertools import combinations, product, permutations

# 리스트 융합해서 permutation 구해보자






demand = int(input())
m, n = map(int, input().split())
pm = [int(input()) for _ in range(m)]
pn = [int(input()) for _ in range(n)]

ans = 0

for i in range(1, m+1):
    # print(list(combinations(pm, i)))
    temp_pm = list(combinations(pm, i))
    temp_pm = [list(e) for e in temp_pm]

    for c1 in temp_pm:
        if sum(c1) == demand:
            ans += 1

    for j in range(1, n+1):
        # print(list(combinations(pn, j)))
        temp_pn = list(combinations(pn, j))
        # print(temp_pn)
        temp_pn = [list(e) for e in temp_pn]


        for c2 in temp_pn:
            if sum(c2) == demand:
                ans += 1

        for c3 in temp_pm:
            for c4 in temp_pn:
                zipped = zip(c3, c4)
                print(*list(zipped))
                for c5 in zipped:
                    # print(c5)
                    # print(sum(c5))
                    if sum(c5) == demand:
                        ans += 1

print(ans)




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