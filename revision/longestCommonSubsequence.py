import numpy as np


# dynamic programming bottom up
# s1 -> represent rows with rows size = n
# s2 -> represent columns with columns size = m
def longestCommonSubsequence(s1, s2, n, m):

    c = -1*np.ones((n+1, m+1))

    for j in range(n+1):
        c[j][0] = 0

    for i in range(m+1):
        c[0][i] = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])

    print("length:", c[n][m], "\n")

    sequence = []
    explored = []

    i = n
    j = m

    while i > 0 and j > 0:
        explored.append([i, j])
        if s1[i - 1] == s2[j - 1]:
            sequence.insert(0, s1[i - 1])
            i -= 1
            j -= 1
        elif c[i-1][j] > c[i][j-1]:
            i -= 1
        else:
            j -= 1

    print("table:\n", c, "\n")
    print("tracing:\n", explored, "\n")
    print("longest common subsequence:", sequence)


s1 = "bdcaba"  # size = 6 -> row
s2 = "abcbdab"  # size = 7 -> column

# s1 = [15, 12, 16, 13, 14, 10, 20, 3, 25, 7]
# s2 = sorted(s1)

# longest common palindromic subsequence
# s1 = "character"
# s2 = s1[::-1]

longestCommonSubsequence(s1, s2, len(s1), len(s2))
