import numpy as np


def fun(m,  n):
    if n == 0:
        return m
    if m == 0:
        return 2*n

    return fun(m-1, n)+fun(m, n-1)


def bottomUp(n, m):
    dp = np.zeros((m+1, n+1))
    for i in range(1, m+1):
        dp[i][0] = 2*i

    for i in range(1, n+1):
        dp[0][i] = i

    for i in range(1, m+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    print(dp[m][n])


m = int(input())
n = int(input())

print(fun(m, n))
bottomUp(m, n)
