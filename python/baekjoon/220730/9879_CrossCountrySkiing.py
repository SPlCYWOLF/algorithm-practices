import sys
sys.stdin = open('input.txt')

M, N = map(int, input().split())
elevations = [list(map(int, input().split())) for _ in range(M)]
waypoint = [list(map(int, input().split())) for _ in range(M)]

