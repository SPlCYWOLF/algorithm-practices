# dfs로 방문하며 visited 체크.
# dfs 종료되면 네트워크 개수 +1

def dfs(cur, n, c, v):
    for j in range(n):
        if not v[j] and c[cur][j]:
            v[j] = 1
            dfs(j, n, c, v)


def solution(n, computers):
    visited = [0] * n
    ans = 0

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            dfs(i, n, computers, visited)
            ans += 1

    return ans

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))


def temp(n):
    if n < 5:
        temp(n+1)
        # n = temp(n+1)
    return n

print(temp(1))