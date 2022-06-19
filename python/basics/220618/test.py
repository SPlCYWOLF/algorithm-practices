import sys
sys.stdin = open('input.txt')


def dfs(c, k, visited):
    global ans, A
    if k == 0:
        temp = max(c) - min(c)
        if temp < ans:
            ans = temp
    else:
        for j in range(len(A)):
            if not visited[j]:
                visited[j] = 1
                dfs(c + [A[j]], k - 1, visited)
                visited[j] = 0

ans = 9999999999
A = list(map(int, input().split()))
K = int(input())
K = len(A) - K

for i in range(len(A)-K):
    visited = [0] * len(A)
    candidate = []
    dfs(candidate, K, visited)

print(ans)