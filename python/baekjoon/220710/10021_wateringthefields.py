import sys
sys.stdin = open('input.txt')
from itertools import combinations

N, C = map(int, input().split())
nodes = [list(map(int, input().split())) for _ in range(N)]
print(nodes)

comb = list(combinations(nodes, 2))
print(comb)

for