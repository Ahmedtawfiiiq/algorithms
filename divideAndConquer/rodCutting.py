import math


# dynamic programming bottom up
def extendedRodCuttingBottomUp(p, n):

    c = [-1]*(n + 1)
    s = [-1]*(n + 1)

    c[0] = 0
    s[0] = 0

    for i in range(1, n + 1):
        q = -math.inf
        for j in range(1, i + 1):
            if p[j] + c[i - j] > q:
                q = p[j] + c[i - j]
                s[i] = j
        c[i] = q

    print(c)
    print(s)
    print("max possible revenue:", c[n])
    cuts = []
    while n > 0:
        cuts.append(s[n])
        n -= s[n]

    print("cuts:", cuts)


p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
n = 8

extendedRodCuttingBottomUp(p, n)
