def is_positive(x, y):
    return x > 0 and y > 0

while True:
    try:
        m, n = map(int, input().split())
        response = ""
        sum_numbers = 0

        if not is_positive(m, n):
            break

        if m > n:
            m, n = n, m

        for i in range(m, n + 1):
            response += str(i) + " "
            sum_numbers += i

        print(f"{response}Sum={sum_numbers}")
    except EOFError:
        break
