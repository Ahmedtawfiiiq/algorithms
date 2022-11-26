# log(n) complexity
def firstSmallestMissing(arr, low, high):
    if low > high:
        return high + 1

    if low != arr[low]:
        return low

    mid = (low + high)//2

    if mid == arr[mid]:
        return firstSmallestMissing(arr, mid + 1, high)
    else:
        return firstSmallestMissing(arr, low, mid)


# sorted array of distinct integers
# arr = [0, 1, 2, 3, 4]
# arr = [0, 1, 2, 6, 9]
# arr = [4, 5, 10, 11]
arr = [0, 1, 2, 3, 4, 5, 6, 7, 10]
result = firstSmallestMissing(arr, 0, len(arr) - 1)
print(result)
