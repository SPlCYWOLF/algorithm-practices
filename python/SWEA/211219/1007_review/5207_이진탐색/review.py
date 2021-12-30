import sys
sys.stdin = open('input.txt')


for tc in range(1, int(input())+1):

    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    # 1. B 리스트 요소들이 A리스트에 있는지 이진탬색으로 확인
    # 2. 한쪽으로 연속 2번이상 이동하면 노 카운트
    # 3. 포함 된 요소들 반환
    