import sys
sys.stdin = open('input.txt')


N = int(input())
tree = [[] for _ in range(N)]

for i in range(N-1):
    parent, child = map(int, input().split())
    if child in tree[1] or child == 1:
        parent, child = child, parent
    tree[parent] += [child]
print(tree)

ans = dict()
for i in range(1, N):
    for child in tree[i]:
        ans.update({child: i})
print(ans)

for i in range(2, N+1):
    print(ans[i])