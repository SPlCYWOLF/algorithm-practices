import sys, heapq
sys.stdin = open('input.txt')

N, C = map(int, sys.stdin.readline().rstrip().split())

# 시간초과
# 크루스칼 알고리즘 활용하여 MST 찾기
# distance값을 오름차순으로 정리 필요
# heapq 활용하여 정렬
# 완성된 heapq를 가지고 연결 가능한 간선값을 축적
# cycle이 형성 안되는것을 확인하기 위해 union-find 알고리즘을 활용
# MST의 간선의 갯수는 N-1 임으로,
# 간선의 갯수가 충족되면 distance의 총 합을, 반대의 경우는 -1을 반환

def find(n):
    global root_table

    if root_table[n] < 0:
        return n
    else:
        root_table[n] = find(root_table[n])
        return root_table[n]

def union(n1, n2):
    global root_table

    p_n1, p_n2 = find(n1), find(n2)
    if p_n1 == p_n2:
        return False
    else:
        root_table[p_n2] = p_n1
        return True

temp = [0] * N
for i in range(N):
    temp[i] = list(map(int, sys.stdin.readline().rstrip().split())) + [i+1]

Q = []
for i in range(N):
    x1, y1, node1 = temp[i]
    for j in range(i+1, N):
        x2, y2, node2 = temp[j]
        d = abs(x1-x2)**2 + abs(y1-y2)**2
        if d >= C:
            heapq.heappush(Q, (d, node1, node2))

if len(Q) < (N-1):
    print(-1)
else:
    root_table = [-1] * (N+1)
    total_cost, road_cnt = 0, 0

    while Q:
        d, n1, n2 = heapq.heappop(Q)
        if union(n1, n2):
            total_cost += d
            road_cnt += 1
        else:
            if road_cnt + len(Q) < N-1:
                print(-1)
                break

        if road_cnt == (N-1):       # 이걸 추가해서 통과
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