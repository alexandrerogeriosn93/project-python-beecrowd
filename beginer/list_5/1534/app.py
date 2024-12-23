while True:
    try:
        n = int(input())
        mat = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i == j:
                    mat[i][j] = 1

                if i == n - j - 1:
                    mat[i][j] = 2

                if i != j and i != n - j - 1:
                    mat[i][j] = 3

        for i in range(n):
            text = ""
            for j in range(n):
                text += str(mat[i][j])
            print(text)

    except EOFError:
        break
