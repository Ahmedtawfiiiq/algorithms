def mergeSortAndCount(arr, l, r):

    count = 0

    if (l < r):

        m = (l+r)//2

        count += mergeSortAndCount(arr, l, m)
        count += mergeSortAndCount(arr, m + 1, r)
        count += mergeAndCount(arr, l, m, r)

    return count


def mergeAndCount(arr, l, m, r):

    left = arr[l:m + 1]
    right = arr[m + 1:r + 1]

    i = j = 0
    k = l

    swaps = 0

    while i < len(left) and j < len(right):
        if (left[i] <= right[j]):
            arr[k] = left[i]
            k += 1
            i += 1

        else:
            arr[k] = right[j]
            k += 1
            j += 1
            swaps += (m + 1) - (l + i)

    while i < len(left):
        arr[k] = left[i]
        k += 1
        i += 1

    while j < len(right):
        arr[k] = right[j]
        k += 1
        j += 1

    return swaps


# arr = [1, 20, 6, 4, 5]
# arr = [8, 2, 46, 9, 2, 7, 3]
# arr = [2, 4, 1, 3, 5]
# arr = [1, 9, 6, 4, 5]
# arr = [38, 27, 43, 3, 9, 82, 10]
arr = [1, 5, 9, 20, 30, 2, 3, 6, 7, 25]
print("original: ", arr)
result = mergeSortAndCount(arr, 0, len(arr) - 1)
print("sorted: ", arr)
print("number of inversions: ", result)
