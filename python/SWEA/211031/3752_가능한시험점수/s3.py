from itertools import combinations
import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    result = []
    res = set()
    for i in range(N+1):
        c = combinations(nums, i)
        # res.add(sum(c))
        result.extend(c)
    for j in range(len(result)):
        res.add(sum(result[j]))
    print(res)