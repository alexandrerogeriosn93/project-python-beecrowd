while True:
    try:
        c = int(input())

        for _ in range(c):
            n, m = map(int, input().split())
            print(len(str(int(n**m))))
    except EOFError:
        break
