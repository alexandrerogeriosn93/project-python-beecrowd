while True:
    try:
        n = int(input())
        start = n // 3
        final = n - start
        mat = [[0 for _ in range(n)] for _ in range(n)]
        aux = 0

        for i in range(n):
            mat[i][i] = 2

        for i in range(n - 1, -1, -1):
            mat[aux][i] = 3
            aux += 1

        for i in range(start, final):
            for j in range(start, final):
                mat[i][j] = 1

        mat[n // 2][n // 2] = 4

        for i in range(n):
            for j in range(n):
                print(mat[j][i], end="")
            print()
        print()
    except EOFError:
        break
