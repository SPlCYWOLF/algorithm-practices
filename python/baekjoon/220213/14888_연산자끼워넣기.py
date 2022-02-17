import sys
sys.stdin = open("input.txt")

# dfs 로 풀이

N = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))

max_val = -1000000000
min_val = 1000000000

def dfs(k, cur, plus, minus, product, divide):
    global max_val, min_val

    if k == N:
        max_val = max(cur, max_val)
        min_val = min(cur, min_val)
        return

    if plus:
        dfs(k + 1, cur + nums[k], plus -1, minus, product, divide)
    if minus:
        dfs(k + 1, cur - nums[k], plus, minus - 1, product, divide)
    if product:
        dfs(k + 1, cur * nums[k], plus, minus, product - 1, divide)
    if divide:
        dfs(k + 1, int(cur / nums[k]), plus, minus, product, divide - 1)

# 깊이, 현재 값, 더하기, 빼기, 곱하기, 나누기 남은 갯수들
dfs(1, nums[0], op[0], op[1], op[2], op[3])
print(max_val)
print(min_val)