import sys
sys.stdin = open('input2.txt')

A = list(map(int, input().split()))

n = len(A)
i = n - 1
result = -1
maximal = 0
k = 0

while (i > 0):
    if (A[i] == 1):
        k = k + 1
        if (k >= maximal):
            maximal = k
            result = i
    else:
        k = 0
    i = i - 1
if A[i] == 1 and k + 1 > maximal:
    result = 0

print(result)