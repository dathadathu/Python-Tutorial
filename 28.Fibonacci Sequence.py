def fib(n):
    a, b = 0, 1
    for i in range(2, n):
        c = a + b
        a = b
        b = c
    return b


print(fib(9))