def indexSearch(arr, low, high):
    if low > high:
        return -1
    else:
        mid = (low + high)//2
        if arr[mid] == mid:
            return mid
        else:
            if arr[mid] > mid:
                return indexSearch(arr, low, mid - 1)
            else:
                return indexSearch(arr, mid + 1, high)


arr = [0, 1, 2, 3, 5, 10, 12]
result = indexSearch(arr, 0, len(arr))
print(result)
