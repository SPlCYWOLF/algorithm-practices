def solution(numbers):

    numbers = list(map(str, numbers))
    numbers = sorted(numbers, reverse=True)
    temp = []
    
    for number in numbers:
        temp.append([number*3, number])
    
    temp = sorted(temp, reverse=True)
    answer = ''.join(map(lambda x:x[1], temp))
    
    return answer

    # 테스트 케이스 한개 통과 안됨