import sys
sys.stdin = open('input.txt')


T = int(input())
for _ in range(T):

    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))

    