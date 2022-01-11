def solution(numbers):

    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=lambda x: x*3, reverse=True)

    answer = str(int(''.join(numbers)))
    # 모든 값이 0일 때(즉, ‘000’을 처리하기 위해) int로 변환한 뒤, 다시 str로 변환로 해결.
    # 이유는 아직 이해 안감
    return answer