import sys
sys.stdin = open('input.txt')


# 소요시간 25분
# S = n * (n+1) / 2     <= 공식 활용!
S = int(input())

i = 1
while True:
    if S == (i * (i+1) / 2):
        print(i)
        break
    elif S < (i * (i+1) / 2):
        print(i-1)
        break
    else:
        i += 1