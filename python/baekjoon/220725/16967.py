import sys
sys.stdin = open('input.txt')

H, W, X, Y = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(H+X))       # B 배열
narr = [arr[i][:W] for i in range(X)] + [[0]*W for _ in range(H-X-1)] + [arr[-1][Y:W+Y]]    # A 배열

for i in range(H):
    if i < X:
        print(*narr[i])
        continue
    if i == H-1:
        print(*narr[-1])
        continue

    for j in range(W):
        if j < Y:
            narr[i][j] = arr[i][j]
            print(arr[i][j], end=' ')
            continue

        narr[i][j] = arr[i][j] - narr[i-X][j-Y]
        print(narr[i][j], end=' ')
    print()



# 패작
# print(*arr[0][:W])
# for i in range(1, H):
#     print(*arr[i+X][Y:W+Y])