def calc_fib(n):
    a, b, c = 1, 2, 3

    while n > 0:
        a, b = b, c
        c = a + b
        n -= c - b - 1

    n += c - b - 1
    return b + n


n = int(input())

print(calc_fib(n))
