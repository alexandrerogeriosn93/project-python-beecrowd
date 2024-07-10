while True:
    try:
        n = int(input())
        values = list(map(int, input().split()))
        max_value = max(values)

        if max_value < 10:
            print(1)
        elif max_value < 20:
            print(2)
        else:
            print(3)
    except EOFError:
        break
