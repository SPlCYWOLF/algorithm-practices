import sys
import heapq

n, base_cost = map(int, sys.stdin.readline().rstrip().split())
nodes = []
for _ in range(n):
    nodes.append(list(map(int, sys.stdin.readline().rstrip().split())))

parents = [i for i in range(n)]
pq = []

for i in range(n):
    for j in range(i+1, n):
        a, b = nodes[i]
        c, d = nodes[j]
        cost = abs(a-c)**2 + abs(b-d)**2
        if cost >= base_cost:
            heapq.heappush(pq, [cost, i, j])

def find(node):
    if parents[node] == node:
        return node
    else:
        parents[node] = find(parents[node])
        return parents[node]
def union(node1, node2):
    root1, root2 = find(node1), find(node2)
    if root1 == root2:
        return False
    else:
        parents[root2] = root1
        return True

total = 0
edge_num = 0
while pq:
    cur_cost, node1, node2 = heapq.heappop(pq)

    if union(node1, node2):
        total += cur_cost
        edge_num += 1
        if edge_num == n-1:
            break

if edge_num == n-1:
    print(total)
else:
    print(-1)




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