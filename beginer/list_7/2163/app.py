def isTheSword(mat, i, j):
    if (mat[i-1][j-1] == 7) and (mat[i-1][j] == 7) and \
       (mat[i-1][j+1] == 7) and (mat[i][j-1] == 7) and \
       (mat[i+1][j-1] == 7) and (mat[i+1][j] == 7) and \
       (mat[i+1][j+1] == 7) and (mat[i][j+1] == 7):
        return True
    else:
        return False

n, m = map(int, input().split())
mat = []

for i in range(n):
    row = list(map(int, input().split()))
    mat.append(row)

for i in range(1, n - 1):
    for j in range(1, m - 1):
        if mat[i][j] == 42 and isTheSword(mat, i, j):
            print((i + 1), (j + 1))
            quit()

print(0, 0)
