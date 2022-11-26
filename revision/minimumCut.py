import math
import numpy as np


def minimumCut(cuts, low, high):
    if low > high:
        return 0
    if dp[low][high] < math.inf:
        return dp[low][high]

    ans = math.inf
    for i in range(low, high + 1):
        ans = min(ans, cuts[high+1]-cuts[low-1] +
                  minimumCut(cuts, low, i-1)+minimumCut(cuts, i+1, high))

    dp[low][high] = ans
    return ans


n = 3
cuts = [0, 2, 4, 7, 10]
dp = np.ones((n+1, n+1))*math.inf
result = minimumCut(cuts, 1, n)
print(dp)
print(result)
