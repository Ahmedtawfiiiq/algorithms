def knapsack(v, w, n, x):

    dp = [0]*(x+1)

    for i in range(1, x + 1):
        for j in range(n):
            if i >= w[j]:
                dp[i] = max(dp[i], v[j] + dp[i - w[j]])

    print(dp)
    print(dp[x])


v = [33, 20, 5, 25]
w = [3, 2, 1, 4]
x = 5
n = len(v)

knapsack(v, w, n, x)
