while True:
    try:
        n = int(input())
        v_max = 0

        for i in range(1, n + 1):
            t, d = map(int, input().split())

            v = d / t

            if v > v_max:
                v_max = v
                print(i)
    except EOFError:
        break
