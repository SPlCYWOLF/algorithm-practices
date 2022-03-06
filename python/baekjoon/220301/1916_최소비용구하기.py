import sys
sys.stdin = open('input.txt')

N = int(input())
M = int(input())
noseon = [list(map(int, input().split())) for _ in range(M)]
depart, arrive = map(int, input().split())

