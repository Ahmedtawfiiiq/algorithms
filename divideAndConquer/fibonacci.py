# recursive
def fibonacci(n):
    # for n >= 2
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# dynamic programming top down
def fibonacciTopDown(n):
    # for n >= 2
    if n == 0 or n == 1:
        return n
    if memorized[n] == 0:
        memorized[n] = fibonacciTopDown(n - 1) + fibonacciTopDown(n - 2)
    return memorized[n]


# dynamic programming bottom up
def fibonacciBottomUp(n):
    memorized[0] = 0
    memorized[1] = 1
    for i in range(2, n + 1):
        memorized[i] = memorized[i - 1] + memorized[i - 2]
    return memorized[n]


memorized = [0]*50
n = 5
# result = fibonacci(n)
# result = fibonacciTopDown(n)
result = fibonacciBottomUp(n)
print(result)
