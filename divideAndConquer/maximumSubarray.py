def maxCrossingSum(arr, l, m, h):

    left_sum = -10000
    sum = 0
    max_left = -1

    # for (int i = m; i > l; i--)
    # {
    #    print(i)
    # }

    # stop when m == l
    for i in range(m, l, -1):
        sum += arr[i]

        if (sum > left_sum):
            left_sum = sum
            max_left = i

    right_sum = -10000
    sum = 0
    max_right = -1

    # for (int i = m + 1; i < h; i++)
    # {
    #    print(i)
    # }

    # stop when m + 1 == h
    for i in range(m + 1, h):
        sum += arr[i]

        if (sum > right_sum):
            right_sum = sum
            max_right = i

    cross_result = [max_left, max_right, left_sum + right_sum]
    print("cross result:")
    print(cross_result, arr[max_left: max_right + 1])
    return cross_result


# Returns sum of maximum sum sub_array in aa[l..h]
def maxSubArraySum(arr, l, h):
    if (l == h):
        result = [l, h, arr[l]]
        print("result:")
        print(result, arr[l: h + 1])
        return result

    m = (l + h) // 2

    left = maxSubArraySum(arr, l, m)
    right = maxSubArraySum(arr, m+1, h)
    cross = maxCrossingSum(arr, l, m, h)

    if (left[2] >= right[2] and left[2] >= cross[2]):
        return left
    elif (right[2] >= left[2] and right[2] >= cross[2]):
        return right
    else:
        return cross


arr = [-2, -5, 6, -2, -3, 1, 5, -6]
n = len(arr)

cross = 0
normal = 0

max_sum = maxSubArraySum(arr, 0, n-1)
print("Maximum contiguous sum is ", max_sum)
