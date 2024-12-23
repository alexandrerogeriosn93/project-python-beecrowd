def calc_fibonacci(n):
    a, b = 0, 1

    if n == 0:
        return 0
    elif n == 1:
        return b
    else:
        for _ in range(1, n):
            c = a + b
            a, b = b, c
        return b


n = int(input())
fib = []

for i in range(1, n + 1):
    fib.append(calc_fibonacci(i))

fib.sort(reverse=True)
print(*fib, sep=" ", end="\n")
