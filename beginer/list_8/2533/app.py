while True:
    try:
        m = int(input())
        numerator = denominator = 0

        for _ in range(m):
            n, c = map(int, input().split())
            numerator += n * c
            denominator += c

        response = numerator / (denominator * 100)
        print(f"{response:.4f}")
    except EOFError:
        break
    except ZeroDivisionError:
        break
