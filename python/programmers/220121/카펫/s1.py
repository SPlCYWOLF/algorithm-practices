# 패작 음 도무지 모르겠다

def solution(brown, yellow):
    # 1. 총 블록 갯수를 기준으로
    temp = brown + yellow
    yaksu = []
    # 2. 모든 공약수 담아서
    for i in range(1, temp+1):
        if temp % i == 0:
            yaksu.append(i)
    
    mid = len(yaksu) // 2
    # 3. 해당 공약수 리스트의 가운데 두 숫자가 정답.
    # 4. 공약수 개수가 홀수 인 경우는 가운데 숫자 두개가 정답?
    if len(yaksu) % 2:
        answer = yaksu[mid:mid+1] * 2
    else:
        answer = sorted(yaksu[mid-1:mid+1], reverse=True)

    return answer