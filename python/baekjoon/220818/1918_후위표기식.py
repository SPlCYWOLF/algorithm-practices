# 참조 : https://velog.io/@younoah/boj-1918
# 스택에는 연산자만 담고 피연산자는 곧 바로 문자열에 합치는 식으로 진행
# 즉 입력받은 문자열을 돌면서
#
# 피연산이면 문자열에 붙인다.
#
# 연산자인경우 :
# 스택이 비어있으면 push
# 스택이 비어있지 않으면 : 연산자의 우선순위가 높은것을 우선 출력해한다. (우선순위는 dictionary로 관리)
# 스택에 마지막(탑) 부터 우선순위 >= 현재 연산자 이면 스택연산자는 pop해서 문자열에 붙이는걸 반복.
# "(" 를 만나거나 스택이 비게 되면 현재연산자를 push한다.
#
# 여는괄호 만나면 그대로 스택에 push.
# 닫는괄호라면 스택에서 여는괄호 만날 떄 까지 팝하여 문자열에 합처넣는다.
#
# 입력받은 문자열을 모두 돌고나서 스택에 남아 있는 연산자들을 모두 pop해서 문자열에 더해준다.

from collections import deque
import sys
sys.stdin = open('input.txt')

ref = {"+": 1, "-": 1, "*": 3, "/": 3, "(": 0}

for _ in range(4):

    given = input()
    ans = []
    stack = []

    for i in range(len(given)):
        letter = given[i]

        if letter == "*" or letter == "/" or letter == "+" or letter == "-":
            while stack:
                if ref[stack[-1]] >= ref[letter]:
                    ans.append(stack.pop())
                else:
                    break
            stack.append(letter)

            continue

        if letter == "(":
            stack.append(letter)
            continue

        if letter == ")":
            while stack[-1] != "(":
                ans.append(stack.pop())
            stack.pop()
            continue

        ans.append(letter)

    while stack:
        ans.append(stack.pop())

    print("".join(ans))





# 패작 3: 하아 ssi..
# 괄호 열리면 bracket +1, 이때 만나는 연산자는 다 BQ에 넣음
# 괄호 하나 닫힐때 마다 BQ에서 연산자 pop()

# 덧셈 or 나눗셈 나오면 다음칸 여는괄호인지 확인 후 여는괄호 아니면 바로 다음에 숫자 다음 출력 되도록 처리
# 마지막에 남는 거 없이 다 출력

# for _ in range(5):
#
#     given = input()
#     ans = []
#     stack, Bstack = [], []
#     bracket = 0
#     go = False
#     for i in range(len(given)):
#
#         if go:
#             go = False
#             ans.append(given[i])
#             ans.append(Bstack.pop())
#             continue
#
#         if bracket:
#
#             if given[i] == "*" or given[i] == "/":
#                 if given[i+1] != "(":
#                     go = True
#                 Bstack.append(given[i])
#                 continue
#
#             if given[i] == "+" or given[i] == "-":
#                 Bstack.append(given[i])
#                 continue
#
#             if given[i] == ")" and Bstack:
#                 bracket -= 1
#                 ans.append(Bstack.pop())
#                 continue
#
#
#
#         if given[i] == "(":
#             bracket += 1
#             continue
#
#         if given[i] == "*" or given[i] == "/":
#             if given[i+1] != "(":
#                 go = True
#             stack.append(given[i])
#             continue
#
#         if given[i] == "+" or given[i] == "-":
#             stack.append(given[i])
#             continue
#
#         if given[i] != "(":
#             ans.append(given[i])
#
#     while stack:
#         ans.append(stack.pop())
#
#     print("".join(ans))




# 패작 2 : index error
# given = input()
# ans = []
#
# Q, BQ = deque(), deque()
# stack, Bstack = [], []
# skip, bskip, bracket = False, False, 0
# for i in range(len(given)):
#     if bracket:
#         if bskip:
#             bskip = False
#             continue
#
#         if given[i] == "*" or given[i] == "/":
#             bskip = True
#             BQ.append(given[i + 1])
#             Bstack.append(given[i])
#             while BQ:
#                 ans.append(BQ.popleft())
#             while Bstack:
#                 ans.append(Bstack.pop())
#             continue
#
#         if given[i] == ")":
#             while BQ:
#                 ans.append(BQ.popleft())
#             while Bstack:
#                 ans.append(Bstack.pop())
#             bracket -= 1
#             continue
#
#         if given[i] == "+" or given[i] == "-":
#             Bstack.append(given[i])
#             continue
#
#         if given[i] == "(":
#             bracket += 1
#             continue
#
#         BQ.append(given[i])
#
#         continue
#
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
#     if given[i] == "+" or given[i] == "-":
#         stack.append(given[i])
#         continue
#
#     if given[i] == "(":
#         bracket += 1
#         ans.append(Q.popleft())
#         continue
#
#     Q.append(given[i])
#
# while Q:
#     ans.append(Q.popleft())
# while stack:
#     ans.append(stack.pop())
#
# print("".join(ans))





# 패작 1 : 틀림
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