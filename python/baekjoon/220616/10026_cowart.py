import sys
sys.stdin = open('input.txt')

# BFS 활용하여 색 영역 확인
# 일단은 사람 따로 소 따로 해답 구해보기

dx = (0, 1, 0, -1)
dy = (-1, 0, 1, 0)

N = int(input())
canvas = [list(input()) for _ in range(N)]
