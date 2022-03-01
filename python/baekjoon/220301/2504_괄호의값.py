
# 출처 https://hongcoding.tistory.com/114
import sys
sys.stdin = open('input.txt')

bracket = list(input())

stack = []
answer = 0
tmp = 1

for i in range(len(bracket)):

    if bracket[i] == "(":
        stack.append(bracket[i])
        tmp *= 2

    elif bracket[i] == "[":
        stack.append(bracket[i])
        tmp *= 3

    elif bracket[i] == ")":
        if not stack or stack[-1] == "[":
            answer = 0
            break
        if bracket[i-1] == "(":
            answer += tmp
        stack.pop()
        tmp //= 2

    else:
        if not stack or stack[-1] == "(":
            answer = 0
            break
        if bracket[i-1] == "[":
            answer += tmp

        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(answer)



# 패작
# 소요 시간 50분
# 더하기 곱하기 타이밍을 어떻게 잡아야할지 못알아냄

# ( = 2   [ = 3
# +   x   불가능   총 세가지 경우
# 닫는 괄호이고, 바로 직전 괄호가 닫는 괄호였으면 ans 에서 곱한다
# 닫는 괄호이고, 바로 직전 괄호가 여는 괄호면 ans 에서 더한다
# 스택 활용

# import sys
# sys.stdin = open('input.txt')
#
#
# nums = input()
# stack = []
# ans = 0
#
# for i in range(len(nums)):
#     temp = 0
#     if len(stack) == 0:                     # 1. 스택이 비었을때
#         if nums[i] == ')' or nums[i] == ']':        # 1-1. 처음부터 닫는 괄호면 0점 처리 후 종료
#             ans = 0
#             break
#         else:                               # 1-2. 처음부터 여는 괄호면 stack에 입력 후 진행
#             stack.append(nums[i])
#     else:                                   # 1. 스택이 안 비었을때
#         if nums[i] == '(' or nums[i] == '[':        # 2. 여는 괄호일때 무조건 일단 넣자
#             stack.append(nums[i])
#         elif stack[-1] == '(' and nums[i] == ')':       # 3. 2점 괄호일 경우 2점
#             stack.pop(-1)
#             ans += 2
#             if nums[i-1] == ')' or nums[i-1] == ']':    # 3-1. 2점 곱하는 경우
#                 ans *= 2
#         elif stack[-1] == '[' and nums[i] == ']':   # 3. 3점 괄호일 경우 3점
#             ans += 3
#         else:                                   # 3. 무효한 경우 0점 처리 후 종료
#             ans = 0
#             break