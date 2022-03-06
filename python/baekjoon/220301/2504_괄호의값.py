
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
            answer += tmp           # 괄호 사이의 값 덧셈 처리
        stack.pop()
        tmp //= 2                   # 포인트

    elif bracket[i] == "]":
        if not stack or stack[-1] == "(":
            answer = 0
            break
        if bracket[i-1] == "[":
            answer += tmp           # 괄호 사이의 값 덧셈 처리
        stack.pop()
        tmp //= 3                   # 포인트

if stack:
    print(0)
else:
    print(answer)



# 패작
# 소요 시간 50분
# 더하기 곱하기 타이밍을 어떻게 잡아야할지 못알아냄

# ( = 2   [ = 3
# +   x   불가능   총 세가지 경우
# 현재 닫는 괄호이고, 스택 마지막 괄호가 여는 괄호고, 바로 직전이 닫는 괄호면 ans 에서 괄호값 만큼 곱하고 스택에서 빼고
# 현재 닫는 괄호이고, 스택 마지막 괄호가 여는 괄호면 ans 에서 더하고 스택에서 빼고
# 현재 여는 괄호고, 바로 직전 닫는 괄호면 ans 를 temp리스트에 넣고 ans 0 으로 초기화 후 괄호 스택에 넣기
# 위에 상황 말고 현재 여는 괄호면 바로 stack에 넣기
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
#
# print(ans)