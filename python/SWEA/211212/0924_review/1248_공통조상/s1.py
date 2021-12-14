import sys
sys.stdin = open('input.txt')


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
    
    # 1. 인접 리스트로 트리 구현
    for i in range(E):
        p = temp[i*2]
        c = temp[i*2+1]
        if not tree[p][0]:
            tree[p][0] = c
        else:
            tree[p][1] = c
        tree[c][2] = p
    
    # 2. 각 노드의 조상들 찾아서 리스트에 모으기
    p1 = search_ance(n1)
    p2 = search_ance(n2)
    
    # 3. 공통된 조상 찾기 (가장 가까운 조상별로 리스트에 들어가 있는걸 참고)
    common_ance = find_common_ance(p1, p2)
    
    # 4. 트리 순회 활용해서 노드 개수 카운트
    pre_order(common_ance)    
    
    print('#{} {} {}'.format(tc, common_ance, cnt))