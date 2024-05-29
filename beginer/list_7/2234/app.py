try:
    h, p = map(int, input().split())
    print(f"{(h / p):.2f}")
except ZeroDivisionError:
    exit()
