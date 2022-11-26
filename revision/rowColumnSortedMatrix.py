# O(n) complexity
def search(mat, n, x):

    # top right element
    i = 0  # row pointer
    j = n - 1  # column pointer
    while (i < n and j >= 0):

        if (mat[i][j] == x):
            return [i, j]

        if (mat[i][j] > x):
            j -= 1

        else:
            i += 1


arr = [[10, 20, 30, 40],
       [15, 25, 35, 45],
       [27, 29, 37, 48],
       [32, 33, 39, 50]]

result = search(arr, len(arr), 29)
print(result)
