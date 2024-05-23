while True:
    try:
        n = int(input())
        values = [int(x) for x in input().split()]
        max_value = max(values)
        res = ""

        if max_value < 10:
            res = 1
        elif max_value < 20:
            res = 2
        else:
            res = 3
        print(res)
    except EOFError:
        break
