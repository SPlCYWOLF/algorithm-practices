# 주어진 부분집합 요소들 중 합이 10이 되는 부분집합 구해라

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
check = [0] * N


def powerset(idx):
    
    if sum(check) == 10:
        for num in check:
            if num:
                print(num, end=' ')
        print()
        return
    if idx == N:
        return
    else:
        check[idx] = arr[idx]
        powerset(idx+1)
        check[idx] = 0
        powerset(idx+1)
        
powerset(0)