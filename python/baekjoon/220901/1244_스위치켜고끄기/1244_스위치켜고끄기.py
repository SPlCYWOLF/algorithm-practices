import sys
sys.stdin = open('input.txt')

def bro(n):
    for i in range(n, N+1, n):
        if switch[i]:
            switch[i] = 0
        else:
            switch[i] = 1

def sis(n):
    if switch[n]:
        switch[n] = 0
    else:
        switch[n] = 1

    for i in range(1, N):
        if 1 > n-i or N < n+i:
            break
        if switch[n-i] == switch[n+i]:
            if switch[n-i]:
                switch[n-i] = 0
            else:
                switch[n-i] = 1
            if switch[n+i]:
                switch[n+i] = 0
            else:
                switch[n+i] = 1
            continue
        break       # 양옆 값 다르면 break

N = int(input())
switch = [0] + list(map(int, input().split()))
SN = int(input())
students = [tuple(map(int, input().split())) for _ in range(SN)]

for student in students:
    if student[0] == 1:
        bro(student[1])
    else:
        sis(student[1])
    print(switch)

for i in range(1, N+1):
    if i % 20 == 0:
        print(switch[i])
    elif i == N:
        print(switch[i])
    else:
        print(switch[i], end=" ")





# def change(num):
#     if switch[num] == 0:
#         switch[num] = 1
#     else:
#         switch[num] = 0
#     return
#
#
# N = int(input())
# switch = [-1] + list(map(int, input().split()))
# students = int(input())
# for _ in range(students):
#     sex, num = map(int, input().split())
#     print(switch)
#     # 남자
#     if sex == 1:
#         for i in range(num, N + 1, num):
#             change(i)
#     # 여자
#     else:
#         change(num)
#         for k in range(N // 2):
#             if num + k > N or num - k < 1: break
#             if switch[num + k] == switch[num - k]:
#                 change(num + k)
#                 change(num - k)
#             else:
#                 break
#
# for i in range(1, N + 1):
#     print(switch[i], end=" ")
#     if i % 20 == 0:
#         print()


# 정답 아웃풋 값 : 0 1 1 1 0 1 1 0






# def bro(n):
#     for i in range(1, N+1):
#         if i % n == 0:
#             if switch[i-1]:
#                 switch[i-1] = 0
#             else:
#                 switch[i-1] = 1
# def sis(n):
#     if n == 1:
#         if switch[0]:
#             switch[0] = 0
#         else:
#             switch[0] = 1
#         return
#
#     for i in range(N):
#         if 0 <= n-i-1 and n+i-1 < N:
#             print(n-i-1, n+i-1)
#             if switch[n-i-1] != switch[n+i-1]:
#                 for j in range(n-i, n+i-1):
#                     if switch[j]:
#                         switch[j] = 0
#                     else:
#                         switch[j] = 1
#
#
# N = int(input())
# switch = list(map(int, input().split()))
# SN = int(input())
# students = [tuple(map(int, input().split())) for _ in range(SN)]
#
# for student in students:
#     if student[0] == 1:
#         bro(student[1])
#     else:
#         sis(student[1])
#     print(switch)
#
# for i in range(N):
#     if i != 0 and i % 20 == 0:
#         print()
#         print(switch[i], end=" ")
#     else:
#         print(switch[i], end=" ")