import sys
sys.stdin = open('input.txt')

def converter(n):
    if n.isnumeric():
        return int(n)
    return n

N = int(input())
M = int(input())
players = [tuple(map(converter, input().split())) for _ in range(M)]
print(players)
players = [0] + players + [0] * (N - len(players))
print(players)