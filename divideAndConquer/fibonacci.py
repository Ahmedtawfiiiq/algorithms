# recursive
def fibonacci(n):
    # for n >= 2
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# dynamic programming top down
def fibonacciTopDown(n):
    # for n >= 2

    memorized = [0]*50

    if n == 0 or n == 1:
        return n
    if memorized[n] == 0:
        memorized[n] = fibonacciTopDown(n - 1) + fibonacciTopDown(n - 2)
    return memorized[n]


# dynamic programming bottom up
def fibonacciBottomUp(n):
    if n == 0 or n == 1:
        return n

    a = 0
    b = 1

    i = 2
    while i <= n:
        temp = a+b
        a = b
        b = temp
        i += 1
    return b


n = 10
# result = fibonacci(n)
# result = fibonacciTopDown(n)
result = fibonacciBottomUp(n)
print(result)
