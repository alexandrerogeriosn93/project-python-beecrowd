while True:
    try:
        n = int(input())

        e1, e2 = map(int, input().split())
        a1 = list(map(int, input().split()))
        a2 = list(map(int, input().split()))

        if n != 1:
            t1 = list(map(int, input().split()))
            t2 = list(map(int, input().split()))

        x1, x2 = list(map(int, input().split()))
        d1 = d2 = 0
        d1 += e1
        d2 += e2

        for i in range(n):
            d1 += a1[i]
            d2 += a2[i]

            if n != 1 and i != n - 1:
                if d1 + t1[i] < d2:
                    d2 = d1 + t1[i]
                elif d2 + t2[i] < d1:
                    d1 = d2 + t2[i]

        d1 += x1
        d2 += x2

        print(d1 if d1 < d2 else d2)
    except EOFError:
        break
