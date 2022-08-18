# ABC* + DE/ -

# 기본 틀 :
# 기본적으로 곱셈과 나눗셈 연산자를 만나기 까지 Q에 숫자들을 기록, 연산자들은 stack에 기록
# 만나면, 다음 숫자 포함 모든 숫자 Q에서 뺴고, 이어서 연산자는 stack에서 모두 뺀다

# 조건 :
# 닫는 괄호를 만나면, 바로 지금까지 Q 출력 후 stack출력

from collections import deque
import sys
sys.stdin = open('input.txt')

given = input()
ans = []

Q, BQ = deque(), deque()
stack, Bstack = [], []
skip, bskip, bracket = False, False, 0
for i in range(len(given)):
    print(bracket)
    if bracket:
        if bskip:
            bskip = False
            continue

        if given[i] == "*" or given[i] == "/":
            bskip = True
            BQ.append(given[i + 1])
            Bstack.append(given[i])
            while BQ:
                ans.append(BQ.popleft())
            while Bstack:
                ans.append(Bstack.pop())
            continue

        if given[i] == ")":
            while BQ:
                ans.append(BQ.popleft())
            while Bstack:
                ans.append(Bstack.pop())
            bracket -= 1
            continue

        if given[i] == "+" or given[i] == "-":
            Bstack.append(given[i])
            continue

        if given[i] == "(":
            bracket += 1
            continue

        BQ.append(given[i])

        continue

    if skip:
        skip = False
        continue

    if given[i] == "*" or given[i] == "/":
        if bracket or given[i+1] == "(":
            stack.append(given[i])
            continue

        skip = True
        Q.append(given[i+1])
        stack.append(given[i])
        while Q:
            ans.append(Q.popleft())
        while stack:
            ans.append(stack.pop())
        continue

    if given[i] == "+" or given[i] == "-":
        stack.append(given[i])
        continue

    if given[i] == "(":
        bracket += 1
        ans.append(Q.popleft())
        continue

    Q.append(given[i])

while Q:
    ans.append(Q.popleft())
while stack:
    ans.append(stack.pop())

print("".join(ans))




# Q = deque()
# stack = []
# skip, bracket = False, 0
# for i in range(len(given)):
#     if skip:
#         skip = False
#         continue
#
#     if given[i] == "*" or given[i] == "/":
#         if bracket or given[i+1] == "(":
#             stack.append(given[i])
#             continue
#
#         skip = True
#         Q.append(given[i+1])
#         stack.append(given[i])
#         while Q:
#             ans.append(Q.popleft())
#         while stack:
#             ans.append(stack.pop())
#         continue
#
#     if given[i] == ")":
#         while Q:
#             ans.append(Q.popleft())
#         while stack:
#             ans.append(stack.pop())
#         bracket -= 1
#         continue
#
#     if given[i] == "+" or given[i] == "-":
#         stack.append(given[i])
#         continue
#
#     if given[i] == "(":
#         bracket += 1
#         continue
#
#     Q.append(given[i])
#
# print("".join(ans))