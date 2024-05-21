# from sympy import isprime

# n = int(input())

# for i in range(n):
#     x = int(input())
#     print(f"{x} eh primo") if isprime(x) else print(f"{x} nao eh primo")

n = int(input())

for i in range(n):
    x = int(input())
    counter = 0

    for j in range(1, x + 1):
        if x % j == 0:
            counter += 1

    print(f"{x} eh primo") if counter == 2 else print(f"{x} nao eh primo")
