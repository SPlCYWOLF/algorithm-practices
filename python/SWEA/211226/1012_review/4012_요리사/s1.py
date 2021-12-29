from itertools import combinations
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def taste(selection, S):
    all_synergy = list(combinations(selection, 2))
    tastepoint = 0
    for synergy in all_synergy:
        x, y = synergy
        tastepoint += S[x][y]
        tastepoint += S[y][x]

    return tastepoint


for tc in range(1, T + 1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]

    sel = list(range(N))
    # N//2 만큼의 원소 개수의 조합을 생성
    cases = list(combinations(sel, N//2))
    diff = 99999999999

    for case in cases:
        # 각 요리의 재료 배정
        food1 = set(case)
        food2 = set(sel) - food1
        # 각 요리의 시너지 값 배정
        taste1 = taste(food1, S)
        taste2 = taste(food2, S)
        # 두 요리의 시너지 값의 차
        tmp_diff = abs(taste1 - taste2)
        # 시너지 값 최소값 생신
        if diff > tmp_diff:
            diff = tmp_diff

    print('#{} {}'.format(tc, diff))