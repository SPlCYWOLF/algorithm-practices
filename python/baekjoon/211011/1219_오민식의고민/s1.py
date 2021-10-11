import sys
sys.stdin = open('input.txt')

'''
미 해결
총 소요 시간 1시간 11분 15초
디버깅 26분
thought process: 17분 25초
인접행렬을 만들고  하나하나 방문하면서 최대 이익 갱신
도착 전까지는 반복적 방문 가능, 고로 visited 필요x
일정횟수 이상 루프가 돌면 무한히 반복가능, 고로 'Gee' 출력
목표지점 도달 못하면 'gg' 출력
'''

def dfs(s, e, p, r):
    global ans
    if r > 500:                         # 재귀가 계속 반복되면
        ans = 'Gee'
        return

    if ans != 'Gee' and ans != 'gg':
        if p < ans:
            return
        if s == e:
            ans = p

        for j in range(len(arr[s])-1):
            dfs(arr[s][j][0], e, p + (arr[arr[s][j][0]][-1] - arr[s][j][-1]), r+1)


N, start, end, M = map(int, input().split())
tmp = [tuple(map(int, input().split())) for _ in range(M)]
reachable = False
loop = False
arr = [[] for _ in range(N)]
ans = -99999999

for i in range(M):                  # 인접 리스트 생성
    arr[tmp[i][0]].append(tmp[i][1:3])
    if end == tmp[i][1]:            # 목표 도시 도달 가능성 확인
        reachable = True
    if start == tmp[i][1]:
        loop = True

revenue = tuple(map(int, input().split()))

for k in range(N):                  # 인접리스트에 노드 별 매출 입력
    arr[k].append(revenue[k])

if reachable:                       # 목표 도시 도달 가능시에만 dfs 진입
    if loop:
        ans = 'Gee'
    else:
        dfs(start, end, arr[0][-1], 0)  # 시작 노드, 끝나는 노드, 이익, 재귀 횟수
else:
    ans = 'gg'                      # 목표 도달 불가능 시, 바로 gg

print(ans)