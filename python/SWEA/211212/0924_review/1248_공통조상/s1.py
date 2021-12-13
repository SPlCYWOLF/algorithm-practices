import sys
sys.stdin = open('input.txt')

# 일단 인접 리스트로 2진트리 생성
# dfs 느낌으로 13에서 출발해서 인접한 노드들 방문하다가
# 현재 위치에서 노드의 크기가 줄어들면 위로 간거니까 부모 노드인거 체크


def search_ance(n):
    s = tree[n][2]
    p = []
    while s != 0:
        p.append(s)
        s = tree[s][2]
    return p

def find_common_ance(p1, p2):
    for i in range(len(p1)):
        for j in range(len(p2)):
            if p1[i] == p2[j]:
                return p1[i]
    return 0

def pre_order(node):
    global cnt
    if node != 0:
        cnt += 1
        pre_order(tree[node][0])
        pre_order(tree[node][1])

for tc in range(1, int(input())+1):
    
    V, E, n1, n2 = map(int, input().split())
    tree = [[0 for _ in range(3)] for _ in range(V+1)]
    temp = list(map(int, input().split()))
    p1, p2 = [], []
    cnt = 0
    
    for i in range(E):
        p = temp[i*2]
        c = temp[i*2+1]
        if not tree[p][0]:
            tree[p][0] = c
        else:
            tree[p][1] = c
        tree[c][2] = p
    
    p1 = search_ance(n1)
    p2 = search_ance(n2)
    common_ance = find_common_ance(p1, p2)
    pre_order(common_ance)    
    
    print('#{} {} {}'.format(tc, common_ance, cnt))