def maxMin(arr, low, high):
    if low == high:  # single element
        return arr[low], arr[low]
    elif low + 1 == high:  # two elements
        # sort the two elements before returning them
        if arr[low] > arr[high]:
            return arr[high], arr[low]
        else:
            return arr[low], arr[high]
    else:
        mid = (low + high)//2
        left = maxMin(arr, low, mid)
        right = maxMin(arr, mid + 1, high)
        return min(left[0], right[0]), max(left[1], right[1])


arr = [4, 1, 2, 3, 5, 6, 8, 9]
min, max = maxMin(arr, 0, len(arr) - 1)
print("minimum:", min)
print("maximum:", max)
