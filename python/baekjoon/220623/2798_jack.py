import sys
sys.stdin = open('input.txt')


def dfs(n, cur):
    global visited, ans, done
    if done:                # 정답이 존재하면 dfs 중단
        return

    if len(cur) == 3:       # 리스트에(주머니) 숫자가 3개있고
        if M == sum(cur):   # 해당 숫자의 합이 주어진 M과 같다면
            done = True     # 정답 발견 선언 후
            ans = sum(cur)  # 정답 기록

        elif sum(cur) < M and abs(M - sum(cur)) < abs(M - ans):     # 숫자의 합이 M보다 작고 기록된 ans보다 M에 근접하면
            ans = sum(cur)                                          # ans 최신화

    else:                                   # 숫자를 3개 뽑지 않았다면
        for j in range(n, N):               # 안 뽑은 카드를 한개씩 뽑고
            if not visited[j]:              # 아직 뽑은 카드가 아니면
                visited[j] = 1              # 뽑았다 기록하고
                dfs(j+1, cur + [nums[j]])   # 해당 숫자를 리스트(주머니)에 넣고 다른 숫자 뽑으러 dfs이동
                visited[j] = 0              # dfs에서 나오면서 뽑았던 카드를 리스트(주머니)에서 꺼내었기 떄문에, 뽑았다는 기록에서 제거


N, M = map(int, input().split())
nums = list(map(int, input().split()))
visited = [0] * N   # 방문 위치 체크용 리스트
done = False        # 정답을 발견 유무 스위치
ans = 9999999999    # 임의 정답 선언 (최초에 무조건적으로 낮은 ans이 올 수 있게 설정)

dfs(0, [])          # 깊이 우선 탐색 활용

print(ans)