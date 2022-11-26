# T(n) = T(n/2) + O(1) => O(n*log(n))
def power(n, p):
    if p == 0:
        return 1
    result = power(n, p//2)
    if p % 2 == 0:
        return result * result
    else:
        return n * result * result


number = 5
p = 3
result = power(5, 3)
print(result)
