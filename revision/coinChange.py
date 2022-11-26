import math


def coinChange(c, n, v):

    m = [math.inf]*(v+1)
    m[0] = 0

    for i in range(1, v+1):
        for j in range(n):
            if i >= c[j]:
                m[i] = min(m[i], 1 + m[i-c[j]])

    print(m)
    print(m[v])


arr = [1, 3, 4]
sum = 6
coinChange(arr, len(arr), sum)
