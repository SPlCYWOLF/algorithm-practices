import sys
sys.stdin = open('input.txt')

def back_dfs(current):
    if current == ".":
        return
    back_dfs(tree[current][0])
    back_dfs(tree[current][1])
    print(current, end="")

def middle_dfs(current):
    if current == ".":
        return
    middle_dfs(tree[current][0])
    print(current, end="")
    middle_dfs(tree[current][1])

def front_dfs(current):
    if current == ".":
        return
    print(current, end="")
    front_dfs(tree[current][0])
    front_dfs(tree[current][1])

# def back_dfs(current):
#     if tree[current][0] != ".":
#         back_dfs(tree[current][0])
#     if tree[current][1] != ".":
#         back_dfs(tree[current][1])
#     print(current, end="")
#
# def middle_dfs(current):
#     if tree[current][0] != ".":
#         middle_dfs(tree[current][0])
#     print(current, end="")
#     if tree[current][1] != ".":
#         middle_dfs(tree[current][1])
#
# def front_dfs(current):
#     print(current, end="")
#     if tree[current][0] != ".":
#         front_dfs(tree[current][0])
#     if tree[current][1] != ".":
#         front_dfs(tree[current][1])


N = int(input())
tree = dict()

for i in range(N):
    center, left, right = map(str, input().split())
    tree.update({center: [left, right]})

front_dfs("A")
print()
middle_dfs("A")
print()
back_dfs("A")