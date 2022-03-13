import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())

# 패작 (시간 초과 DP 써야하는듯)
# 소요시간 30분
# 동전 종류 오름차순 정렬
# dfs 돌리면서 k 값 나오면 ans에 cnt 값 저장
# dfs 들어갈때 마다 cnt 축적
# cnt가 최소값보다 같거나 커지면 바로 컽
# ans 에서 가장 작은 값 == 정답

coins = [int(input()) for _ in range(n)]
coins = sorted(coins, reverse=True)
ans = [9999999999]

def dfs(cur, cnt):
    if cur == 0:
        ans.append(cnt)
    else:
        if cnt >= min(ans):
            return

        for coin in coins:
            if cur - coin >= 0:
                dfs(cur-coin, cnt+1)

dfs(k, 0)
print(ans)
print(min(ans))