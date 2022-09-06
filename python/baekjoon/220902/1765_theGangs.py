from collections import defaultdict
import sys
sys.stdin = open('input.txt')

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
temp = {"1": {"원수": {"4", "2"}, "친구": {"7", "8"}}}

N = int(input())
M = int(input())
group = defaultdict(dict)
for i in range(M):
    relation, p, q = input().split()
    # if relation == "F":
    #     if q in group:
    #         group[q] |= {"친구": p}
    #         continue
    #     group[p] |= {"친구": q}

    if relation == "E":
        if q in group and group[q]["원수"]:
            for wonsu in group[q]["원수"]:
                print(wonsu)

        group[p].update({"원수": q})

print(group)
group["1"].update({"친구": "5"})
print(group)