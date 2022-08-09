import sys
sys.stdin = open('input.txt')

# 전위, 중위 순회 둘 다 알아보고 가능성 있는 리스트 저장
# 전위와 준위 순회 일치하는 리스트가 정답 트리 리스트.
# 해당 정답 트리 리스트 기준으로 후위 순회 결과 출력

def findTree(n):
    rn = preorder[n]
    visited[rn] = 1

    # 좌측 subtree
    lrn = preorder[n+1]
    if not visited[lrn] and lrn not in inorder[inorder.index(rn):]:
        tree[rn][0] = lrn
        visited[lrn] = 1
        findTree(n + 1)
    
    # 우측 subtree
    lTreeNodeCnt = len(inorder[:inorder.index(rn)])
    if lTreeNodeCnt and lTreeNodeCnt+1 < total_node:
        rrn = preorder[n + lTreeNodeCnt + 1]
        if not visited[rrn]:
            if rn in inorder[:inorder.index(rootNode)]:    # left tree 를 확인중이면
                if rrn in inorder[n:inorder.index(rootNode)]:   # 현재 노드의 우측 && 루트노드의 좌측 여부 확인
                    tree[rn][1] = rrn
                    visited[rrn] = 1
                    findTree(n + lTreeNodeCnt + 1)
            else:                                           # right tree를 확인중이라면
                if rrn in inorder[inorder.index(rn):]:          # 현재 노드의 우측 여부 확인
                    tree[rn][1] = rrn
                    visited[rrn] = 1
                    findTree(n + lTreeNodeCnt + 1)


T = int(input())
for _ in range(T):

    total_node = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    rootNode = preorder[0]
    tree = [[0, 0] for _ in range(total_node+1)]
    visited = [0] * (total_node + 1)

    findTree(0)

    print(tree)