def knapsack(v, w, n, x):

    dp = [0]*(x+1)

    for i in range(x + 1):
        for j in range(n):
            if (w[j] <= i):
                dp[i] = max(dp[i], dp[i - w[j]] + v[j])

    print(dp)


v = [33, 20, 5, 25]
w = [3, 2, 1, 4]
x = 5
n = len(v)

knapsack(v, w, n, x)
