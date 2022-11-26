import numpy as np


def subSetSum(arr, n, sum):

    c = np.zeros((n + 1, sum + 1))

    for i in range(n + 1):
        c[i][0] = True

    for i in range(1, sum + 1):
        c[0][i] = False

    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if j < arr[i-1]:
                c[i][j] = c[i-1][j]
            else:
                c[i][j] = (c[i-1][j] or
                           c[i-1][j-arr[i-1]])

    print(c)

    i = n
    j = sum

    result = []

    while i > 0 and j > 0:
        if c[i][j] != c[i-1][j]:
            result.append(arr[i-1])
            j -= arr[i-1]
            i -= 1
        else:
            i -= 1

    print("result:", result)

    return c[n][sum]


# arr = [3, 4, 5, 2]
# sum = 6

arr = [3, 2, 7, 1]
sum = 6
subSetSum(arr, len(arr), sum)
