def solution(numbers):

    numbers = list(map(str, numbers))
    numbers = sorted(numbers, reverse=True)
    temp = sorted(numbers, key=lambda x:x[0], reverse=True)
    print(temp)
    answer = ''.join(temp)
    
    return answer