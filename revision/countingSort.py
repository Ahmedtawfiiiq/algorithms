def countingSort(arr, n, k, r):

    c = [0] * (k+1)

    for i in range(0, n):
        c[arr[i]] += 1

    for i in range(1, k+1):
        c[i] += c[i - 1]

    print(c)

    # prefix sum

    # if r[0] >= 1:
    #     print(c[r[1]] - c[r[0]-1])
    # else:
    #     print(c[r[1]])

    b = [0] * n

    for i in range(n - 1, -1, -1):
        b[c[arr[i]] - 1] = arr[i]
        print(b)
        c[arr[i]] -= 1

    return b


# arr = [4, 2, 2, 8, 3, 3, 1]
arr = [4, 1, 3, 4, 3]
print("before:", arr)
result = countingSort(arr, len(arr), k=max(arr), r=[1, 3])
print("after: ", result)
