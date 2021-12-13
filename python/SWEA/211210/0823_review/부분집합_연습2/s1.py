arr = [1, 2, 3, 4]
N = len(arr)
check = [0] * N


def powerset(idx):
    if idx == N:
        print(*check)
        return
    else:
        check[idx] = 1
        powerset(idx+1)
        check[idx] = 0
        powerset(idx+1)
        
powerset(0)