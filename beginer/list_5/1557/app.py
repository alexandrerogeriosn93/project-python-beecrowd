while (n := int(input())) > 0:
    mat = [[0 for _ in range(n)] for _ in range(n)]
    mat[0][0] = 1

    for i in range(n):
        if i >= 1:
            mat[i][0] = mat[i - 1][0] * 2

        for j in range(1, n):
            mat[i][j] = mat[i][j - 1] * 2

    len_str = len(str(mat[n - 1][n - 1]))

    for i in range(n):
        for j in range(n):
            mat[i][j] = str(mat[i][j])

            while len(mat[i][j]) < len_str:
                mat[i][j] = " " + mat[i][j]

        response = " ".join(mat[i])
        print(response)
    print()
