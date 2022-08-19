import sys
sys.stdin = open('input.txt')

# 숫자 스택에 집어넣음
# 연산자 만나면 두개 빼서 해당 연산 시킴
# 결과값 stack에 넣음
# 반복

N = int(input())
given = input()
nums = [int(input()) for _ in range(N)]

stack = []
for letter in given:
    if letter.isalpha():
        stack.append(nums[ord(letter) - ord("A")])
        continue

    n1, n2 = stack.pop(), stack.pop()
    if letter == "+":
        stack.append(n2 + n1)
    elif letter == "-":
        stack.append(n2 - n1)
    elif letter == "*":
        stack.append(n2 * n1)
    else:
        stack.append(n2 / n1)

ans = stack.pop()
print(f'{ans:.2f}')

# 성공 1 : 근데 정말 쓸데없이 길다
# def add(n1, n2):
#     return n1 + n2
# def minus(n1, n2):
#     return n2 - n1
# def multiply(n1, n2):
#     return n1 * n2
# def divide(n1, n2):
#     return round(n2 / n1, 2)
#
# ref = {
#     "+": add,
#     "-": minus,
#     "*": multiply,
#     "/": divide
# }
#
# N = int(input())
# given = input()
# done = []
#
# n_ref = {}
# for i in range(len(given)):
#     n = given[i]
#     if n not in done and n != "-" and n != "+" and n != "*" and n != "/":
#         done.append(n)
#         n_ref[n] = int(input())
#
#
# stack = []
# k = 0
# for i in range(len(given)):
#     letter = given[i]
#
#     if letter == "*" or letter == "/" or letter == "+" or letter == "-":
#         calculated_num = ref[letter](stack.pop(), stack.pop())
#         stack.append(calculated_num)
#         continue
#
#     stack.append(n_ref[letter])
#     k += 1
#
# ans = stack.pop()
# print(format(ans, ".2f"))