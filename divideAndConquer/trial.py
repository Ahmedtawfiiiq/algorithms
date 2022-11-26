import numpy as np


def knapSack(v, w, n, m):

    c = -1*np.ones((n+1, m+1))

    for i in range(n+1):
        c[i][0] = 0

    for i in range(m+1):
        c[0][i] = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if w[i-1] > j:
                c[i][j] = c[i-1][j]
            else:
                c[i][j] = max(c[i-1][j-w[i-1]] + v[i-1], c[i-1][j])

    print(c)


v = [33, 20, 5, 25]
w = [3, 2, 1, 4]
x = 5

knapSack(v, w, len(v), x)
