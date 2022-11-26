# T(n) = 2T(n/2) + O(1) => O(n)
def minimum(arr, low, high):
    if low == high:
        return arr[low]
    else:
        mid = (low + high)//2
        left = minimum(arr, low, mid)
        right = minimum(arr, mid+1, high)
        return min(left, right)


arr = [0, 7, 1, 2, 3, 4, 5]
result = minimum(arr, 0, len(arr) - 1)
print(result)
