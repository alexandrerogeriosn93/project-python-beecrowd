while True:
    try:
        x, y = map(int, input().split())

        if x == y:
            break

        print("Crescente" if x < y else "Decrescente")
    except EOFError:
        break
