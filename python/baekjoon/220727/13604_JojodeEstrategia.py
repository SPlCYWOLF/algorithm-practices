import sys
sys.stdin = open('input.txt')

J, R = map(int, input().split())
victories = list(map(int, input().split()))

winner, max_point = 0, 0
for i in range(J):
    point = sum(victories[i:R*J:J])
    # print(victories[i:R*J:J])
    if point >= max_point:
        max_point = point
        winner = i+1
print(winner)