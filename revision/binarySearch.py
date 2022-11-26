def binarySearch(arr, low, high, key):
    if low > high:
        return -1
    else:
        mid = (low + high)//2
        if arr[mid] == key:
            return mid
        else:
            if arr[mid] > key:
                return binarySearch(arr, low, mid - 1, key)
            else:
                return binarySearch(arr, mid + 1, high, key)


# sorted array
arr = [1, 2, 3, 4, 5, 6, 7, 8, 10]
result = binarySearch(arr, 0, len(arr) - 1, 11)
print(result)
