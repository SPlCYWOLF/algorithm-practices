# N 의 약수중 K 번째로 작은 수를 출력
# 작은 약수부터 구해가며 cnt 갱신, K번 찾으면 종료 후 출력

# 14분07초 소요

import sys
sys.stdin = open('input.txt')


def finder(i, n):
    global cnt
    if not n % i:
        cnt += 1


def solution():
    N, K = map(int, input().split())
    for i in range(1, N+1):
        finder(i, N)
        if cnt == K:
            return i
    return 0

cnt = 0
print(solution())