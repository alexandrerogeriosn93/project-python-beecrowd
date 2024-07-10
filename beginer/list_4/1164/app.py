def calc_divider(n):
    response = 0

    for i in range(1, n - 1):
        if i != n:
            if n % i == 0:
                response += i

    return response

n = int(input())

for i in range(n):
    x = int(input())

    print(f"{x} eh perfeito" if x == calc_divider(x) else f"{x} nao eh perfeito")
