# T(n) = 2T(n/2) + O(1)
def maximumDivideAndConquer(arr, low, high):
    if low == high:
        return arr[low]

    mid = (low + high)//2
    left = maximumDivideAndConquer(arr, low, mid)
    right = maximumDivideAndConquer(arr, mid + 1, high)
    if left > right:
        return left
    else:
        return right


# log(n) complexity
def maximum(arr, low, high):
    if low == high:
        return arr[low]

    mid = (low + high)//2

    if arr[low] > arr[mid]:
        return maximum(arr, low, mid - 1)
    elif arr[mid] < arr[mid + 1]:
        return maximum(arr, mid + 1, high)
    else:
        return arr[mid]


# the given array is circularly shifted k positions to the right
# sorted => 2, 3, 4, 5, 6, 7, 9
# rotated => 9, 2, 3, 4, 5, 6, 7

# arr = [6, 7, 9, 2, 3, 4, 5]
arr = [4, 5, 6, 10, 1, 2, 3]
result = maximum(arr, 0, len(arr) - 1)
print(result)
