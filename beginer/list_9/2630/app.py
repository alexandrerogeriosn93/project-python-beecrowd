while True:
    try:
        t = int(input())

        for i in range(1, t + 1):
            conversion = input()
            r, g, b = list(map(int, input().split()))
            res = 0

            match conversion:
                case "eye":
                    res = int(0.3 * r + 0.59 * g + 0.11 * b)
                case "mean":
                    res = int((r + g + b) // 3)
                case "min":
                    res = min(r, g, b)
                case "max":
                    res = max(r, g, b)

            print(f"Caso #{i}: {res}")
    except EOFError:
        break
