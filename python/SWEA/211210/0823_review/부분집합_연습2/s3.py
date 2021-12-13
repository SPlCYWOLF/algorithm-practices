

def powerset(arr, idx, nums):
    if idx == len(arr):
        if sum(nums) == 10:
            print(*nums)
        return
    
    powerset(arr, idx+1, nums+[arr[idx]])
    powerset(arr, idx+1, nums)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
powerset(arr, 0, [])