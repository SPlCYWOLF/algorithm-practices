from collections import defaultdict
import sys
sys.stdin = open('input.txt')

# 패작 2 :
# 유니온 파인드 그래프 알고리즘을 활용하여, 친구는 같은 그래프로,
# 원수는 다른 그래프로,
# 원수의 원수는 같은 그래프로 연결시키는 작업 후
# 그래프형 리스트를 set로 변환 후, 해당 set의 길이 == answer

from collections import defaultdict

def find(n):
    if parent[int(n)] == n:
        return n
    else:
        parent[int(n)] = find(parent[int(n)])
        return parent[int(n)]


def merge(p, q):
    pp, pq = find(p), find(q)
    if pp == pq:
        return      # p의 부모와 q의 부모가 같다면, 이미 연결되어있음으로 return
    else:
        parent[int(pq)] = pp     # pq의 부모노드를 pp로 바꿈


N = int(input())
M = int(input())

wonsu_dict = defaultdict(dict)
parent = [0] + ([0] * N)
for i in range(M):
    relationship, p, q = input().split()
    parent[int(p)], parent[int(q)] = p, q

    if relationship == "F":
        merge(p, q)
        continue

    if p in wonsu_dict:
        tp = wonsu_dict[p][0]
        merge(tp, q)
    elif q in wonsu_dict:
        tq = wonsu_dict[q][0]
        merge(p, tq)

    wonsu_dict |= {p: q}
    wonsu_dict |= {q: p}

print(parent)
ans = set(parent[1::])
print(len(ans))







# 패작 1 :
# F : p & q 는 친구
# E : p & q 는 원수

# 친구의 친구는 친구
# 친구의 원수는 원수
# 원수의 원수는 친구

# 하나하나 학생 돌면서
# 딕셔너리에{번호: {원수: 번호, 친구: 번호} }
    # 친구의 key 값이 존재하면 내 번호를 친구 key의 value에 추가
        # 만약 없다면, 본인의 key값을 추가하여 친구 번호를 value로 추가
    # 원수의 key 값이 존재하면 원수들을 모두 확인해서
        # 해당 원수만의 그룹이 있다면, 그쪽의 친구 key의 value에 본인 추가
        # 없다면 본인만의 그룹 생성하여 원수 key의 value에 원수 추가

# 최종 딕셔너리의 key값 개수 = 정답

# N = int(input())
# M = int(input())
# group = defaultdict(dict)
# for i in range(M):
#     relation, p, q = input().split()
#     if relation == "F":
#         if q in group:
#             group[q]["친구"] |= {p}
#             continue
#         group[p] |= {"친구": {q}}
#
#     if relation == "E":
#         if q in group:
#             group[q]["원수"] |= {p}
#
#             if "원수" in group[q].keys():
#                 for wonsu in group[q]["원수"]:
#                     group[wonsu] |= {"친구": {p}}
#
#         else:
#             # group[p].update({"원수": q})
#             group[p] |= {"원수": {q}}
#
# print(group)