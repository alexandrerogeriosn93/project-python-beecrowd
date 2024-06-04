while True:
    try:
        n, min_height, max_height = map(int, input().split())
        print(sum(1 for _ in range(n) if min_height <= int(input()) <= max_height))
    except EOFError:
        break
