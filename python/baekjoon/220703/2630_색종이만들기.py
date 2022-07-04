import sys
sys.stdin = open('input.txt')

# 원소를 비교.
# 동일하지 않다면, 4개로 자르고 하나씩 원소를 비교
# 무한 반복

def dfs(n, r, c):
    global b_cnt, w_cnt
    target = paper[r][c]

    for i in range(r, r+n):
        for j in range(c, c+n):
            if paper[i][j] != target:
                dfs(n//2, r, c)
                dfs(n//2, r+n//2, c)
                dfs(n//2, r, c+n//2)
                dfs(n//2, r+n//2, c+n//2)
                return
    if target:
        b_cnt += 1
    else:
        w_cnt += 1


N = int(input())
paper = [tuple(map(int, input().split())) for _ in range(N)]
b_cnt, w_cnt = 0, 0

dfs(N, 0, 0)   # 종이의 총 길이, 위치 r & c

print(w_cnt)
print(b_cnt)