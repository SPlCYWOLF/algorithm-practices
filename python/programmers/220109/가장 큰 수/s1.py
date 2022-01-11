def comb(k, num, v, t):
    global answer
    if len(answer) and num[0] < max(answer)[0]:
        return

    if k == len(t):
        answer.append(num)
        return
    for i in range(len(t)):
        if not v[i]:
            v[i] = 1
            comb(k+1, num+t[i], v, t)
            v[i] = 0


def solution(numbers):
    global answer
    # 숫자 가져와서 str으로 바꾸고 더해나가기
    temp = list(map(str, numbers))
    visited = [0] * len(temp)
    comb(0, '', visited, temp) # 깊이, 완성숫자, 방문정보, 인풋 리스트 정보
    
    answer = list(map(int, answer))
    answer = str(max(answer))

    return answer

answer = []
numbers = [3, 30, 34, 5, 9]

print(solution(numbers))

# 왠만하면 재귀는 쓰지말자.