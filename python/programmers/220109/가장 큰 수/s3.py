def solution(numbers):

    numbers = list(map(str, numbers))
    numbers = sorted(numbers, reverse=True)
    numbers = sorted(numbers, key=lambda x:x[0] ,reverse=True)
    print(numbers)
    for i in range(len(numbers)-1):
        # 뒤에 원소 길이가 더 짧고,
        # 현재원소의 2번째 원소와 뒤 원소의 크기를 비교해서 뒤 원소의 크기가 더 크면 바로 자리 바꾸기
        if len(numbers[i]) > len(numbers[i+1]) and numbers[i][1] < numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
    print(numbers)
    answer = ''.join(numbers)
    
    return answer