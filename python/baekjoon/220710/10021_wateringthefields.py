import sys, heapq
sys.stdin = open('input.txt')

N, C = map(int, sys.stdin.readline().rstrip().split())  # 연결하고 싶은 필드 개수, 최소 지불 비용

# 시간초과
# 크루스칼 알고리즘 활용하여 MST 찾기
# distance값을 오름차순으로 정리 필요
# heapq 활용하여 정렬
# 완성된 heapq를 가지고 연결 가능한 간선값을 축적
# cycle이 형성 안되는것을 확인하기 위해 union-find 알고리즘을 활용 : union(n1, n2)
# n1과 n2가 최상위 부모노드를 공유한다면, 얘들이 연결되면 cycle이 형성되어버림
# MST의 간선의 갯수는 N-1 임으로,
# 간선의 갯수가 충족되면 distance의 총 합을, 반대의 경우는 -1을 반환

def find(n):            # 파인드 함수
    global root_table

    if root_table[n] < 0:   # 부모노드가 없을 경우 자기 자신을 반환
        return n
    else:                   # 있을 경우 해당 부모노드의 부모노드 탐색
        root_table[n] = find(root_table[n])
        return root_table[n]    # 최상위 부모노드 반환

def union(n1, n2):      # 유니온 함수
    global root_table

    p_n1, p_n2 = find(n1), find(n2) # 각 노드에 대해 부모 노드 탐색
    if p_n1 == p_n2:    # 부모 노드가 같을 시 cycle 형성되었다는 뜻,
        return False    # 고로 false 반환
    else:
        root_table[p_n2] = p_n1     # p_n1를 p_n2의 부모노드로 설정
        return True

temp = [0] * N
for i in range(N):      # 각 인풋 필드 위치 받아오기 : [x, y, 필드 식별 번호]
    temp[i] = list(map(int, sys.stdin.readline().rstrip().split())) + [i+1]
print(temp)

Q = []      # 크루스칼 알고리즘을 위해 최소 힙 자료구조로 건설비용(간선)기준 오름차순 정렬
for i in range(N):
    x1, y1, node1 = temp[i]
    for j in range(i+1, N):
        x2, y2, node2 = temp[j]
        d = abs(x1-x2)**2 + abs(y1-y2)**2   # 건설 비용
        if d >= C:                          # 최소 지불 비용과 대조
            heapq.heappush(Q, (d, node1, node2))
print(Q)

if len(Q) < (N-1):  # MST의 조건(간선 개수 = 노드개수 - 1) 미달 시 컽
    print(-1)
else:               # MST일 가능성 있으면 진행
    root_table = [-1] * (N+1)       # 각 노드의 최상위 부모 노드 기록용
    total_cost, road_cnt = 0, 0

    while Q:        # 최소 건설 비용부터 차례대로 꺼내서
        d, n1, n2 = heapq.heappop(Q)
        if union(n1, n2):               # cycle 형성 안되는지 union-find 알고리즘으로 확인
            total_cost += d             # 건설 비용 축적
            road_cnt += 1               # 연결된 간선 개수 축적
            # print(root_table)
        else:
            if road_cnt + len(Q) < N-1:     # MST생성 가능성 없어지면 컽
                print(-1)
                break

        if road_cnt == (N-1):       # MST 완성(연결된 간선 개수 충족)되면 종료
            print(total_cost)
            break









# 1차 패작
# import sys
# sys.stdin = open('input.txt')
# from itertools import combinations
#
# # 조합으로 모든 노드간의 간선 구하고 저장
# # 크루스칼 알고리즘으로 최소신장트리 구하기
#
# N, C = map(int, input().split())
# input_nodes = [list(map(int, input().split())) for _ in range(N)]
# ans = 0
# # print(input_nodes)
#
# comb = list(combinations(input_nodes, 2))
# # print(comb)
#
# nodes = dict()
# for coordinates in comb:
#     x, y = coordinates
#     distance = (x[0]-y[0])**2 + (x[1]-y[1])**2
#
#     temp_x, temp_y = [str(x) for x in x], [str(y) for y in y]
#     node_key = (''.join(temp_x), ''.join(temp_y))
#     nodes[node_key] = distance
# # print(nodes)
# distances = sorted(nodes.values())
#
# visited = []
# for dist in distances:
#     if dist >= C:
#         dist_node = list(nodes.keys())[list(nodes.values()).index(dist)]
#         print(dist_node)
#         if dist_node not in visited and dist_node[::-1] not in visited:
#             visited += [(dist_node)]
#             ans += dist
#
# # print(visited)
#
# print(ans)