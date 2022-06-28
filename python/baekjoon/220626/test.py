def countingSort(array):
    L = len(array)
    occurances_cnt = [0] * (max(array)+1)
    # count the occurances of each element in the arrary
    for i in range(L):
        occurances_cnt[array[i]] += 1
    print(occurances_cnt)

    # adding each element to the right of it accumulatively
    for i in range(1, len(occurances_cnt)):
        occurances_cnt[i] += occurances_cnt[i-1]
    print(occurances_cnt)

    # shifting the whole arrary to right side one index
    for i in range(len(occurances_cnt)-1, 0, -1):
        occurances_cnt[i] = occurances_cnt[i-1]
    occurances_cnt[0] = 0
    print(occurances_cnt)

    # check for the distorting index number for each element in the original array
    # and record the starting index on a new array
    output = [0] * len(array)
    for i in range(len(array)):
        output[occurances_cnt[array[i]]] = array[i]
        occurances_cnt[array[i]] += 1
    print(output)
    print("-------------------------------------------")
    return output

data = [4, 2, 2, 3, 3, 1, 10]
print(data)
print()
print("Sorted Array in Ascending Order: ")
print(countingSort(data))