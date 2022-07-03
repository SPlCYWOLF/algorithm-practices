import sys
import pprint
sys.stdin = open('input.txt')


def dfs(n, s):
    target = paper[s][s]
    for i in range(n):
        for j in range(n):
            if paper[i][j] != target:
                dfs(N//2, )



N = int(input())
paper = [tuple(map(int, input().split())) for _ in range(N)]
pp = pprint.PrettyPrinter()
pp.pprint(paper)

dfs(N, 0)   # 종이의 총 길이, 종이의 시작길이 위치