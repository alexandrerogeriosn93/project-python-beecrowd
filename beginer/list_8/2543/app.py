while True:
    try:
        n, i = map(int, input().split())
        print(sum(1 for _ in range(n) if tuple(map(int, input().split())) == (i, 0)))
    except EOFError:
        break
