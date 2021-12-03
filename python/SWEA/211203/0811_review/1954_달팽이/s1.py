import sys
sys.stdin = open('input.txt')


# 2번째 풀이
for tc in range(1, int(input())+1):

    N = int(input())

    table = [[0]*N for _ in range(N)]   # 2차원 배열 생성

    x, y = 0, 0         # 좌표값 초기화
    table[x][y] = 1     # 시작지점에 첫번째 숫자 입력

    for idx in range(2, N*N+1):

        # 인덱스 범위를 벗어나지 않는다는 조건문을 어떻게 작성할까..
        if y+1 < N and table[x][y+1] == 0:                # 우측이동시
            y += 1
        elif x+1 < N and table[x+1][y] == 0:              # 아래이동시
            x += 1
        elif y-1 >= 0 and table[x][y-1] == 0:              # 좌측이동시
            y -= 1
        elif x-1 >= 0 and table[x-1][y] == 0:              # 위쪽이동시
            x -= 1

        table[x][y] = idx

    print('#{}'.format(tc))
    for i in range(N):
        print(*table[i])



# 1번째 풀이

# 2차원 배열 만들고
# 방향 델타값 활용해서 한칸씩 전진하면서 벽 만나면 방향 바꾸기

dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

for tc in range(1, int(input())+1):

    N = int(input())
    
    arr = [[0] * N for _ in range(N)]
    i, j = 0, 0
    num = 1

    if N != 1:
        while arr[i][j+1] == 0:
            arr[i][j] = num        
            k = 0
                
            while j < N-1 and arr[i][j+1] == 0:
                num += 1
                i = i + dr[k]
                j = j + dc[k]
                
                arr[i][j] = num

            k += 1
            while i < N-1 and arr[i+1][j] == 0:
                num += 1
                i = i + dr[k]
                j = j + dc[k]
                
                arr[i][j] = num
            
            k += 1
            while 0 < j and arr[i][j-1] == 0:
                num += 1
                i = i + dr[k]
                j = j + dc[k]
                
                arr[i][j] = num

            k += 1
            while 0 < i and arr[i-1][j] == 0:
                num += 1
                i = i + dr[k]
                j = j + dc[k]
                
                arr[i][j] = num
    
    else:
        arr[0][0] = 1
    
    print('#{}'.format(tc))
    for row in arr:
        for single in row:
            print(single, end=' ')
        print()
    
            
            
            

                    
        
        
    
            
    
    