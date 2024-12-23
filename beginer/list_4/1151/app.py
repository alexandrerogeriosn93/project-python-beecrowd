def calc_fibonacci(n):
    a, b = 0, 1

    if n == 0:
        return 0
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a, b = b, c
        return b


n = int(input())

for i in range(0, n):
    fib = calc_fibonacci(i)
    print(fib, end=[" ", "\n"][i == n - 1])
