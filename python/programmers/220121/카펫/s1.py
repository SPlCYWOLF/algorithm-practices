def solution(brown, yellow):
    # 갈색 노란색 숫자 더함
    # 위 값의 약수 구해서 리스트에 정리
    # 가운데 두개가 정답
    temp = brown + yellow
    yaksu = []
    for i in range(1, temp+1):
        if temp % i == 0:
            yaksu.append(i)
            
    mid = len(yaksu) // 2
    if len(yaksu) % 2:
        answer = yaksu[mid:mid+1] * 2
    else:
        answer = sorted(yaksu[mid-1:mid+1], reverse=True)

    return answer