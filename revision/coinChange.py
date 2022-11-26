import math


def coinChange(c, n, v):

    m = [-1]*(v+1)
    m[0] = 0

    for i in range(1, v+1):
        m[i] = math.inf
        for j in range(1, n+1):
            if i >= c[j - 1]:
                m[i] = min(m[i], 1 + m[i-c[j - 1]])

    print(m)
    print(m[v])


arr = [1, 3, 4]
sum = 6
coinChange(arr, len(arr), sum)
